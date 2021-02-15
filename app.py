import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get(
    "MONGO_DBNAME")  # grab the database
# configure the actual connection string
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recommendations")
def recommendations():
    books = mongo.db.recommendations.find()
    return render_template("recommendations.html", books=books)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie to indentify the user
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        books = mongo.db.recommendations.find()
        return render_template("profile.html", books=books, username=username)

    return redirect(url_for("login"))


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        # define our dict
        book = {
            "category_name": request.form.get("category_name"),
            "name": request.form.get("name"),
            "author": request.form.get("author"),
            "publisher": request.form.get("publisher"),
            "genre": request.form.get("genre"),
            "publication_date": request.form.get("publication_date"),
            "book_cover": request.form.get("book_cover"),
            "shop_link": request.form.get("shop_link"),
            "recommended_by": session["user"],
        }
        mongo.db.recommendations.insert_one(book)
        flash("Book Successfully Added")
        return redirect(url_for("recommendations"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_book.html", categories=categories)


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "name": request.form.get("name"),
            "author": request.form.get("author"),
            "publisher": request.form.get("publisher"),
            "genre": request.form.get("genre"),
            "publication_date": request.form.get("publication_date"),
            "book_cover": request.form.get("book_cover"),
            "shop_link": request.form.get("shop_link"),
            "recommended_by": session["user"],
        }
        mongo.db.recommendations.update({"_id": ObjectId(book_id)}, submit)
        flash("Book Successfully Updated")

    book = mongo.db.recommendations.find_one({"_id": ObjectId(book_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_book.html", book=book, categories=categories)


@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    mongo.db.recommendations.remove({"_id": ObjectId(book_id)})
    flash("Book Successfully Removed")
    return redirect(url_for("recommendations"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
