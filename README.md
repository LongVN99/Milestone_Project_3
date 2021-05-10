# BookReviews

Enjoy reading, BookReviews can help you find the book you like. 

## How It Works

By logging in users can see recommendations books and recommend book on BookReviews.

<a name="demo"></a>

## Demo

You can visit BookReviews right away by clicking
[here](https://bookreviews-heroku.herokuapp.com/)
<img src='mockups/DEMO_BookReviews.png'></img>

## Database design
<img src='mockups/data_design.png'></img>

## User Experience (UX)
To make the web simple for the user to understand and to give necessairy information about how to use the web and about the book provided.

- ### Users
    -   #### New user Goals
        1. As a new user, I want to know what the web is.(BookReviews/home)
        2. As a new user, I want register an account.(register)
        3. As a new user, I want to look for recommendations books provides by BookReviews. (recommendations)

    -   #### Returning user Goals.
        1. As a returning user, I would like to be able to edit or delete any content added by me.

    -   #### Frequent user Goals
        1. As a frequent user, I want to log in my account. (account)
        2. As a frequent user, I want to views book on multiple device. (responsive)
        3. As a frequent user, I want to recommend book. (recommendations)
        4. As a frequent user, I want to check my recommended books. (profile)

- ### Owners
    1. As a owner, I want my website to be preferable and accessible.
    2. As a owner, I want to earn money on each book purchased via a link from the site.

-   ### Design
    -   #### Colour Scheme
        *   Main color used are shade of orange, yellow, blue, black and white (the Colour Scheme is provide by bootsrap theme)
    -   #### Typography
        *   I use Merriweather with Sans Serif for all contents in this game. (the Typography is provide by bootsrap theme)

## Features

* Allow user to view on multiple device
* Allow user register, log in and log out his/her account
* Allow user to understand how to use and what the BookReviews provides.
* Allow user to go direly to a web (Amazon.com) where user can buy the book.
* Allow user to recommend book

### Future features
1. Reviews - Allow user write reviews

<a name="browsersuport"></a>
## Browser support

-   ### The browser version that fully supports.
    * Chrome *(36.0)*
    * Edge *(10.0)*
    * Firefox *(16.0)*
    * Opera *(23.0)*
    * Safari *(9.0)*

##  Code
- My theme is taken from this website. [Startbootstrap creative](https://startbootstrap.com/theme/creative)
- I also inspired certain way to code from Code Institute. [Acknowledgements](#Ack)

## Testing
-   [W3C Markup Validator](https://validator.w3.org/) - [Results](validator/homepage.png)

### Testing User Stories from User Experience (UX) Section
-   #### New user Goals
    1. As a new user, I want to know what the web is.(BookReviews/about) - PASS
        * By clicking on BookReviews user can see information of BookReviews.

    2. As a new user, I want register an account.(register) - PASS
        * User can register an account, data will be stored in mongoDB's Database (users)

    3. As a new user, I want to look for recommendations books provides by BookReviews. (recommendations) - PASS
        * In BookReviews's recommendations page user can see all the book in BookReviews's Database.

-   #### Returning user Goals.
    1.  As a returning user, I would like to be able to edit or delete any content added by me. - PASS
        * Edit and delete button appear.
        * Reviews information from each book will also be shown.
        
        
-   #### Frequent user Goals
    1. As a frequent user, I want to log in my account. (account)  - PASS
        * user can log in his account if he has already registered.

    2. As a frequent user, I want to views book on multiple device. (responsive)  - PASS
        * Each device have its own style which make the web responsive. So user can view on a mobile phone or a computer.
        * Click [here](#demo) to see how does the responsive look like.

    3. As a frequent user, I want to recommend book. (recommendations) - PASS
        * By clicking on recommended button, the recommended count will be increased.
        * User must login before to recommend book.
        * User can recommend the same book once per account.

    4. As a frequent user, I want to check my recommended books. (profile)  - PASS
        * After logging in BookReviews users are able to check their profile which displays book(s) that this user accout added to BookReviews recommendations.

### Features Testing
* Edit and Remove buttons appear correctly if the book is added by the logged in account.
* Form fields is validated by type (text, url, date)
* Books which are added by logged in account appears in profile page.
* Users are able to Edit, Add, Remove books which are added by themself on the website after logging in.

### Further Testing
* Registered account stores in mongoDB. [MongoDB](https://www.mongodb.com/)
* Every button has the same style to increase the look and feel of user when changing pages.
* All links were tested. Internal links all work. External links all work and open in new window.
* The data displayed correctly, all buttons link to a correct destination.
* All the pages are responsive on all screen sizes.
* If user hasn't log in and enters in the url an link which are allowed for logged user such as add_book, this user will be direct to log in page with a message "You must log in first".

### Bugs
#### Fixed
* Add book doesn't display correctly on mobile (responsive fixed)
* Footer is always on the bottom of the web. (add 100vh for body content)
* User who hasn't log in can't enter the page which is allowed for logged account only

## Strategy

The goal in the design was to make it as easy as possible for non experience user to be able understand. User can find all needed information about the book from BookReviews.

## Technologies

**Languages:**
* [HTML5:](https://www.w3schools.com/html/default.asp)
    - HTML5 was used to code the content of the website.
* [CSS:](https://www.w3schools.com/css/default.asp)
    - CSS3 was used to style the content.
* [JavaScript:](https://www.w3schools.com/js/default.asp)
    - JavaScript was used to style the significant interactive functionality.
* [Python:](https://www.w3schools.com/python/default.asp)
    - Python was used for the project back-end functions. Flask and Python is used to build route functions.

**Tools and Libraries:**
* [W3C Validator:](https://validator.w3.org/)
    - The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to clear syntax errors.
* [Font-Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
* [Flask:](https://flask.palletsprojects.com/)
    - web application framework used to create functions with Python that are injected into html templates. 
* [jQuery:](https://jquery.com/)
    - jQuery library was used to simplify the JavaScript.
* [HTML and CSS Beautifier:](http://minifycode.com/html-beautifier/)
    - HTML and CSS was used to format the codes to make it more readable.
* [JSHint](https://jshint.com/) 
    - Used to test/validate JavaScript Code.
* [PEP8 Online Checker:](http://pep8online.com/)
    - P8P was used to verify that python coding conventions were applied to meet requirements.
* [figma:](https://www.figma.com/)
    - Diagram software used to create the database schema and data manipulation operations diagrams.
* [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

## Structure

The navigation bar is structured to get the right information as quickly as possible. The website itself is structured in hope of user feels ease while viewing and the database is also structured in order and in a clear way.

## Known Issues
* Unable to define if users provide the correct informations
* If book_cover is a wrong link the image will not be displayed

## Deployment
### `How to open this project`
1. Copy this link "https://bookreviews-heroku.herokuapp.com/"
1. Paste and open on a browser

### Connecting the Application to MongoDB
1. Logged into my MongoDB account.
1. With the "Clusters" tab selected, I clicked on "Connect"
1. Selected "Connect your application"
1. Selected "Python" as the "Driver" and "Version" "3.6 or later".
1. Copied the connection string and pasted it in my env.py file editing it to include my dbname and my user password.
1. Created an instance of PyMongo and passed the application to that instance as below:
-       mongo = PyMongo(app)

### Local Deployment
* On the [GitHub Repository](https://github.com/LongVN99/Milestone_Project_3), click on the '↓ Code' button.
* Copy the link to clone the repository using the HTTPS tab.
* In your preferred IDE CLI, navigate to the directory you would like to clone to.
* Type `git clone ` followed by the URL you copied from step 3 and press enter.
* Once cloned, all files from workspace will be visible.
* You will need to create an `env.py` that had previously been added to the `.gitignore` file.
* To test type `python3 app.py runserver` into the CLI and open the 8080 port.
* Finally using git you can push this to your own GitHub repository.

### Heroku Deployment
*In Gitpod:*

* Once the Flask App is created, the following OS default environment variables were set in the `env.py` file:
    * "IP", with the IP address you want the app to run on.
    * "PORT", with the specified port.
    * "SECRET_KEY", with a value generated from a random key generator.
    * "MONGO_URI", with the connection string from MongoDB.
    * "MONGO_DBNAME", with the database name

* This file along with all other sensitive files were added to the `.gitignore` file.
* To specify the Python package dependencies to Heroku the requirements.txt file was created using the command `pip3 freeze --local > requirements.txt`.
* The Procfile was also created using the command `echo web: python app.py` to tell Heroku that the `app.py` file uses the Python language.

*In Heroku:*

* A new app was created with the name 'bookreviews-heroku'.
* In the 'Deploy Tab' GitHub was connected using the repository name.
* In the 'Settings' tab of Heroku, the Configuration Variables (Config Vars) were added (these are the 'key: value' pairs that were declared in the `env.py` file).
* Back in the 'Deploy' tab the 'Enable Automatic Deployment' button was clicked to allow automatic updates from GitHub.
* The branch was then deployed from the master.

*In Gitpod:*

* The Mongo database is then wired up to the Flask app by adding the Mongo links to the default environment variables.

### Adding A requirements.txt File

To add the list of Python dependencies that the project needs in order to run successfully and detect the language:

* `pip3 freeze --local > requirements.txt` - command in the terminal to create a requirements.txt file, 

### Adding A Procfile

To inform Heroku on how to run the application and which file runs it the **Procfile** was installed:

* `echo web: python app.py > Procfile` - with a capital 'P' command in the terminal to redirect the echo command.

## Credits
- ### Content

* Inspiration and base code was derived from the Mini Project section of the [Code Institute](https://courses.codeinstitute.net/) course.
Code was modified to better fit my needs. 

## Content
* Book's informations are based on two main sources, namely [Amazon](https://www.amazon.com/) and [Wikipedia](https://www.wikipedia.org/).

<a name="Ack"></a>
-   ### Acknowledgements
    * Inspiration and base code was derived from the Mini Project section of the [Code Institute](https://courses.codeinstitute.net/) course.
Code was modified to better fit my needs.
    * Special thanks to my mentor Oluwafemi Medalen for supporting me during the project
