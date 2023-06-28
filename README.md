## Table of Contents

- [Executive Summary](#executive-summary)
  - [Market Analysis](#market-analysis)
  - [Marketing and Sales Strategy](#marketing-and-sales-strategy)
  - [Operations and Management](#operations-and-management)
  - [Financial Plan](#financial-plan)
  - [Conclusion](#conclusion)
- [Marketing](#marketing)
  - [Social Media](#social-media)
  - [Mailing List](#mailing-list)
- [User Goals](#user-goals)
- [Site Owner Goals](#site-owner-goals)
- [User Experience](#user-experience)
- [User Stories](#user-stories)
- [Wireframes](#wireframes)
- [Design](#design)
  - [Colors](#colors)
  - [Fonts](#fonts)
  - [Structure](#structure)
    - [Website pages](#website-pages)
    - [AWS](#aws)
    - [Database](#database)
    - [Models](#models)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Validation](#validation)
- [Testing](#testing)
  - [Manual testing](#manual-testing)
  - [Automated testing](#automated-testing)
  - [Tests on various devices](#tests-on-various-devices)
  - [Browser compatibility](#browser-compatibility)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)


## Business Plan  
### Executive Summary:

ThrottleMotocross is a web-based platform that connects bikers to shop and share tips and tricks. It offers a convenient ecommerce shop for purchasing motocross products. In addition, ThrottleMotocross features a blog with the latest news and tips on the Motocross culure, as well as a contact page for inquiries and support.

Our target market is Motocross bikers of all skill levels and demographics, as well as beginners looking for a streamlined solution to het start and get some of the latest product on the market. We aim to differentiate ourselves from competitors by offering a more user-friendly and intuitive platform.

In terms of revenue, ThrottleMotocross will generate income through the sale of products in our ecommerce shop. We will also explore potential partnerships and sponsorships with bike-related brands to further monetize the platform.

Overall, ThrottleMotocross aims to become the go-to destination for Motocross enthusiast.

### Market Analysis:

The golf industry is a multi-billion euro industry, with a large and dedicated consumer base. While traditional methods of booking tee times (such as calling the club or booking in-person) are still popular, there is a growing trend towards online booking platforms. This shift towards online booking presents a significant opportunity for Teetime to establish itself as a leading player in the market.

ThrottlerMotocross will face other online Motocross but, we believe that our user-friendly platform and wide range of products in our ecommerce shop will differentiate us from competitors and make us a preferred choice for Motocross bikers.

### Marketing and Sales Strategy:

ThrottleMotocross will utilize a combination of online and offline marketing tactics to reach our target market. These tactics will include:

Online advertising through social media platforms such as Facebook and Instagram
Content marketing through our blogs
Partnerships and sponsorships with golf-related brands
Public relations efforts to generate press coverage and raise awareness of ThrottleMotocross.
In terms of sales, our primary focus will be on converting website visitors into customers through the use of persuasive copy and calls-to-action.

### Operations and Management:

ThrottlesMotocross will be operated and managed by a small team of experienced professionals. The team will consist of a CEO, CTO, and marketing and sales staff.

In terms of operations, we will utilize a cloud-based platform to host the website and software, as well as a payment gateway for processing transactions. We will also utilize third-party fulfillment centers to handle the storage, packing, and shipping of products purchased through our ecommerce shop.

#### Financial Plan:

ThrottlesMotocross will generate revenue through the sale of products in our ecommerce shop. In terms of expenses, the main cost will be marketing and advertising efforts to drive traffic to the website and attract customers.

ThrottlesMotocross will initially be funded through a combination of personal investment and a small seed round of funding. As the business grows, we will explore additional funding options such as venture capital or a larger round of financing.


In terms of profitability, we expect to break even within the first year of operation and achieve profitability in the second year.

### Conclusion:

ThrottlesMotocross is a unique and innovative platform that aims to connect golfers with Motocross rider to find whatever suits their need while connecting and sharing tricks and tips.With strong growth potential and a clear revenue model, we believe that ThrottlesMotocross has the potential to become a leading player in the Motoctoss industry.
<hr>

## Marketing  

### Social Media  
The web app "throttlesmotocross" has a presence on both Facebook and Instagram. The Facebook page serves as a platform to promote post updates on the future plans and products, and share user-generated content. The Instagram page primarily focuses on showcasing Motocross activities and events, highlighting new products in the shop, and providing a behind-the-scenes look at the company. These social media accounts allow users to stay informed and connected with the "throttlesmotocross" community.



### User Goals

### Site Owner Goals

## User Experience

### Target Audience

### User Reqirements and Expectaions

### User Stories

#### User

#### Returning User

#### Site Owner

### Kanban, Epics & User Stories

## Design

## Models

### User Model

## Website pages

- The site consists of the following pages:
  - Home
  - Product List
  - Product Expanded
  - Basket
  - Checkout
  - Checkout Success
  - Blog
  - Blog expanded
  - Contact
  - Register
  - Profile
  - Login
  - Logout
  - Reset Password
  - Register
  - 404

## AWS 

I am using AWS S3 buckets to store my data. S3 is a highly scalable and durable cloud storage service provided by Amazon Web Services. It allows me to easily store and retrieve large amounts of data, and its built-in security features provide added protection for my files. I chose S3 for its scalability, durability, and security features.

<details><summary>See AWS Images</summary>

## Database

I built my database using PostgreSQL. It's a powerful and open-source object-relational database system that is known for its reliability, robustness, and performance. I chose it because it provides a flexible tool for efficiently managing and organizing my data.

<hr>

# Structure

The site was designed for the user to be familiar with the layout such as a navigation bar along the top of the pages and a hamburger menu button for smaller screen.

The footer contains all relevant social media links that the business has so the user can visit any social media site and follow the business there to expand the businesses followers, likes and shares.
It contains an email sign up form and useful links as well as contact information.


| Key        | Name         | Type        |
| ---------- | ------------ | ----------- |
| PrimaryKey | user_id      | AutoField   |
|            | password     | VARCHAR(45) |
|            | last_login   | VARCHAR(45) |
|            | is_superuser | BOOLEAN     |
|            | username     | VARCHAR(45) |
|            | first_name   | VARCHAR(45) |
|            | last_name    | VARCHAR(45) |
|            | email        | VARCHAR(45) |
|            | is_staff     | BOOLEAN     |
|            |              |             |
|            | is_active    | BOOLEAN     |
|            | date_joined  | VARCHAR(45) |

### User Profile Model

| Key        | Name                 | Type          |
| ---------- | -------------------- | ------------- |
| PrimaryKey | user_profile_id      | AutoField     |
| ForeignKey | user                 | User model    |
|            | default_phone_number | CharField[20] |
|            | default_address1     | CharField[80] |
|            | default_address2     | CharField[80] |
|            | default_town_city    | CharField[40] |
|            | default_county       | CharField[80] |
|            | default_postcode     | CharField[20] |
|            | default_country      | CharField[40] |

### Product Model

| Key        | Name        | Type           |
| ---------- | ----------- | -------------- |
| PrimaryKey | product_id  | AutoField      |
|            | code        | CharField[50]  |
|            | brand       | CharField[50]  |
|            | name        | CharField[50]  |
|            | description | TextField      |
|            | has_sizes   | BooleanField   |
|            | price       | DecimalField   |
| ForeignKey | category    | Category model |
|            | rating      | DecimalField   |
|            | image       | ImageField     |

### Category Model

| Key        | Name          | Type      |
| ---------- | ------------- | --------- |
| PrimaryKey | category_id   | AutoField |
|            | name          | Char[254] |
|            | friendly_name | Char[254] |

### Order Model

| Key        | Name            | Type               |
| ---------- | --------------- | ------------------ |
| PrimaryKey | order_id        | AutoField          |
|            | order_number    | CharField[40]      |
| ForeignKey | user_profile    | User profile Model |
|            | full_name       | CharField[50]      |
|            | email           | EmailField[254]    |
|            | phone_number    | CharField[20]      |
|            | address1        | CharField[80]      |
|            | address2        | CharField[80]      |
|            | town_city       | CharField[40]      |
|            | postcode        | CharField[20]      |
|            | county          | CharField[80]      |
|            | country         | CharField[40]      |
|            | date            | DateTimeField      |
|            | delivery_cost   | DecimalField[6]    |
|            | order_total     | DecimalField[10]   |
|            | grand_total     | DecimalField[10]   |
|            | original_basket | TextField          |
|            | stripe_pid      | CharField          |

### OrderLineItem Model

| Key        | Name             | Type            |
| ---------- | ---------------- | --------------- |
| PrimaryKey | OrderLineItem_id | AutoField       |
| ForeignKey | order            | Order Model     |
| ForeignKey | product          | Product Model   |
|            | product_size     | CharField[2]    |
|            | quantity         | IntegerField    |
|            | line_item_total  | DecimalField[6] |

### Post Model

| Key        | Name           | Type                |
| ---------- | -------------- | ------------------- |
|            | title (unique) | Char[200]           |
|            | slug (unique)  |                     |
| PrimaryKey | post_id        | AutoField           |
| ForeignKey | author         | User model          |
|            | created_date   | DateTime            |
|            | updated_date   | DateTime            |
|            | content        | TextField           |
|            | featured_image | Cloudinary<br>image |
|            | excerpt        | TextField           |
|            | status         | Integer             |

### Comment Model

| Key        | Name         | Type                                   |
| ---------- | ------------ | -------------------------------------- |
| ForeignKey | post         | Post model<br>Cascade on<br>delete     |
|            | name         | CharField[80]                          |
|            | email        | EmailField                             |
|            | body         | TextField                              |
|            | created_date | DateTimeField<br>auto*now*<br>add_true |
|            | approved     | BooleanField<br>default False          |
|            |              |                                        |
|            |              |                                        |
|            | Meta         | created_on                             |

### ContactUs Model

| Key        | Name         | Type             |
| ---------- | ------------ | ---------------- |
| PrimaryKey | message_id   | AutoField        |
|            | created_date | DateTimeField    |
| ForeignKey | user         | User model       |
|            | name         | CharField        |
|            | email        | EmailField       |
|            | phone        | PhoneNumberField |
|            | body         | TextField        |

## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Django

### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/)
- [Balsamiq](https://balsamiq.com/)
- [Bootstrap v5.2](https://getbootstrap.com/)
- [Cloudinary](https://cloudinary.com/)
- [Favicon.io](https://favicon.io)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
- [Font Awesome](https://fontawesome.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Google Fonts](https://fonts.google.com/)
- [Heroku Platform](https://id.heroku.com/login)
- [AWS](https://aws.amazon.com/)
- [jQuery](https://jquery.com)
- [Postgres](https://www.postgresql.org/)
- [Summernote](https://summernote.org/)
- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  - [JShint](https://jshint.com/)
  - [CI Python Liner(PEP8)](https://pep8ci.herokuapp.com/)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
  - [Wave Validator](https://wave.webaim.org/)

### Manual testing

1. As a site user I want to see a Motocross scheme to site

   | **Step** | **Expected result** | **Actual Result** |
   |-------------|------------|---------------------|
   | Visit page:https://ci-pp5-throttles-motocross-2c6aa11127d2.herokuapp.com/| Home page tells about the wht the site represent with photos to match | Work as Expected | 

   <details><summary>Screenshots</summary>
   <img src="">
   </details>

2.	As a Site User	I CAN navigate across the site 	SO THAT I CAN can access all parts of the site  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Navbar | Click on any link in the navbar to be brought to a relevant page, shop for example | Be brought to shop to view all products after clicking all products in the navbar | Works as expected  

<details><summary>See Images</summary>
<img src=" ">
<img src=" ">
</details>  


11. As a site user I want to get messages when I enter, update or delete data entries

| **Step**                 | **Expected Result**             | **Actual Result** |
| ------------------------ | ------------------------------- | ----------------- |
| Submit Loginform         | Logged in message will display  | Works as expected |
| Submit update form       | Updated message will display    | Works as expected |
| Sumit logout             | Logged out message will display | Works as expected |
| Submit delete Enrollment | Deleted message will display    | Works as expected |
| Submit Enrollmet         | Enrolled message will display   | Works as expected |

  <details><summary>Screenshots</summary>
    <img src="docs/testing/test-story-login-message.JPG">
    <img src="docs/testing/test-story-logout-message.JPG">
    <img src="docs/testing/test-story-edit-message1.jpg">
    <img src="docs/testing/test-story-delete-message.jpg">
    <img src="docs/testing/test-story-enrollment-message.JPG">
  </details>

12. As a site owner I want the user to be able to send us messages/emails through a contact form
    | **Step** | **Expected Result** | **Actual Result** |
    |------------|---------------------|-----------------|
    | Got to 'Get Registered' click on 'Contact' | Contact form will be displayed with message field | Works as expected |

    <details><summary>Screenshots</summary>
    <img src="docs/testing/test-navbar-contact-page.JPG">
    </details>

13. I want my site to be fully responsive

    | **Step**                                         | **Expected Result**                                            | **Actual Result** |
    | ------------------------------------------------ | -------------------------------------------------------------- | ----------------- |
    | Change device screen size using chrome dev tools | The web functionality remains the same on various screen sizes | Works as expected |

    <details><summary>Screenshot</summary>
    <img src="docs/testing/test-story-response-tablet.png">
    <img src="docs/testing/test-story-responsive-mobile.png">
    </details>

14. As a site owner want user to see data entry vaildation when registering
    |**Step** | **Expected Result** | **Actual Result**
    |------------ | ------------ | ------------ |
    |Click on the 'Log in' on the nav bar and 'Register' from the drop-down menu | Displays Registration page | Works as expected |
    |Input username shorter than 4 characters (eg. xyz) | Prevents registration. Shows warning message to lenghten username text | Works as expected |
    |Input username which has already been taken (eg. Admin) | Prevents registration. Displays 'A user with that username already exists.' message | Works as expected |
    |Input incorrect format of email | Shows warning message to include '@' in the email. Prevents registration | Works as expected |
    |Input 'newuser12' password | Prevents registration. Displays 'The password is too similar to the username' message | Works as expected |
    |Input '12345678' as a password | Prevents registration. Displays 'This password is entirely numeric' message | Works as expected |
    |Input 'testing' as a password | Prevents registration. Displays 'This password is too short. It must contain at least 8 characters' message | Works as expected |
    |Input two different values in 'Password' and 'Password (again)' fields | Prevents registration. Displays 'You must type the same password each time.' message | Works as expected |

    <details><summary>Screenshots</summary>
    <img src="docs/testing/test-story-common-pass.png">
    <img src="docs/testing/test-story-register-email.png">
    <img src="docs/testing/test-story-register-pass-characters.png">
    <img src="docs/testing/test-story-register-pass-sim.png">
    <img src="docs/testing/test-story-register-same-pass.png">
    <img src="docs/testing/test-story-registration-input validation.png">
    <img src="docs/testing/test-story-user-exist.png">
    </details>

15. As a site user I want to see a blog list
    | **Step** | **Expected Result** | **Actual Result** |
    |------------|---------------------|-------------------|
    | Go to blog on navbar | A list of blog post will display | Works as expected |
    <details><summary>Screenshots</summary>
    <img src="docs/testing/test-story-pagination2.png">
    </details>

16. As a site user to want to read blog details
    | **Step** | **Expected Result** | **Actual Result** |
    |------------|---------------------|-------------------|
    | Click on a blog image in blog list | Blog details will display | Works as expected |
    <details><summary>Screenshots</summary>
    <img src="docs/feature/feature-blog-detailse.png">
    </details>

17. As a site user I want to have blog commenting options
    | **Step** | **Expected Result** | **Actual Result** |
    |------------|---------------------|-------------------|
    | Login, click on blog post | Comment form will display for commenting | Works as expected |
    <details><summary>Screenshots</summary>
    <img src="docs/feature/feature-login-required.JPG">
    <img src="docs/testing/test-story-login-message.JPG">
    <img src="docs/testing/test-story- blog commenting.png">
    </details>

18. As a owner I want to control commnets posted
    | **Step** | **Expected Result** | **Actual Result** |
    |------------|---------------------|-------------------|
    | User submit Comment | Comment waiting approval message is displayed | Works as expected |
    <details><summary>Screenshots</summary>
    <img src="docs/testing/test-story-blog-commenting-approve.jpg">
    </details>

19. As a return user I want the site to remember me
    | **Step** | **Expected Result** | **Actual Result** |
    |------------|---------------------|-------------------|
    | Comment | 2 | Works as expected |
    <details><summary>Screenshots</summary>
    <img src="docs/feature/feature-login-required.JPG">
    <img src="docs/testing/test-story-login-message.JPG">
    </details>

## Bugs

List of bugs found and fixes used ti mitigate them.

-

## Configuration

### Google emails

To set up the project to send emails and to use a Google account as an SMTP server, the following steps are required:

1. Create an email account at google.com, login, click you user icon and then on 'Manage Your Google Account'
2. Click on the Security tab
3. Turn on 2-step verification and follow the steps to enable
4. Click on App passwords, click on Select app and choose Other
5. Give your app a name and click on 'Generate'
   <br>![App password]()
6. A 16 digit password will be generated, note the password down
7. Set the below variables within the settings.py file to successfully send emails
   <br><code>EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'</code>
   <br><code>EMAIL_HOST = 'smtp.gmail.com'</code>
   <br><code>EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')</code>
   <br><code>EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')</code>
   <br><code>EMAIL_PORT = '587'</code>
   <br><code>EMAIL_USE_TLS = True</code>
8. Set up the variables EMAIL_HOST_USER and EMAIL_HOST_PASSWORD in your Render application Config vars

## Deployment

### Heroku

This application has been deployed from GitHub to Heroku by following the steps:

### Forking the GitHub Repository

1. Go to the GitHub repository
2. Click on Fork button in top right corner
3. You will then have a copy of the repository in your own GitHub account.

### Making a Local Clone

1. Go to the GitHub repository
2. Locate the Code button above the list of files and click it
3. Highlight the "HTTPS" button to clone with HTTPS and copy the link
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone <span>https://</span>github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone

[Back to Table Of Contents](#table-of-content)

### Heroku Deployment

[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com
<details>
<img src="docs/heroku/heroku-create-app.JPG">
</details>

2. Create an app, give it a name similar to project name, and select a region
<details>
<img src="docs/heroku/heroku-overview.JPG">
</details>

3. Under resources search for postgres, and add a Postgres database to the app

4. Create and ElephantSqul account and set up a plan with in your region
   <details>
   <img src="docs/heroku/sql.JPG">
   </details>

5. Copy Url database instance from Sql account and store it in the env.py enviroment variable (os.environ["DATABASE_URL"]="<copiedURL>")

6. Add a your secret key to env.py enviroment variable os.environ["SECRET_KEY"]="my_super^secret@key"

7. Import env.py to settings.py add Data base and sercert key variable to settings.py file

8. Add localhost, and wildlifers.herokuapp.com to the ALLOWED_HOSTS variable in settings.py
<details>
<img src="docs/heroku/debug-false.JPG">
</details>
9. Migrate change to manage.py

10. Add Secret key and Database url to Heroku Config vars

11. Add PORT 8000 to config vars to avoid deployment failure

12. Set DEBUG value to False
<details>
<img src="docs/heroku/debug-false.JPG">
</details>

13. Set X_FRAME_OPTION ='SAMEORIGIN'

14. Run pip3 freeze > requirements.txt so that file are updated before deployment

15. Run "python3 manage.py showmigrations" to check the status of the migrations

16. Run "python3 manage.py migrate" to migrate the database

17. Check config vars for DISABLE_COLLECTSTATIC=1 is removed

18. Go to deploy in the Heroku app
    <details>
    <img src="docs/heroku/heroku-deploy.JPG">
    </details>

19. Clik Deploy

20. View build logs for error
     <details>
     <img src="docs/heroku/heroku-build-log.JPG">
     </details>

21. Click app to view website

## Credits

### Media

Media images were referenced from <a href="https://www.pexels.com/">Pexels</a> , <a href="https://unsplash.com/">Upsplash</a> and <a href="http://www.freepik.com/">Freepik</a>.

- [404-background](assets/images/404er.jpeg): <a href=" https://www.pexels.com/photo/an-apple-and-a-dumbbell-on-a-clipboard-8154260/" >Pexels</a>
  Photo by: <a href="https://www.pexels.com/@alesiakozik/">Alesia Kozik</a>
- [signup-page-background](assets/images/signupimage.jpeg): <a href="https://www.pexels.com/photo/          personal-male-trainer-with-overweight-female-client-in-fitness-center-6455927/">Pexels</a>
  Photo by: <a href="https://www.pexels.com/@julia-larson/">Julian Larson</a>
- [hero-image](assets/images/heroimage.jpg): <a href="https://www.freepik.com/premium-photo/sport-couple-doing-plank-exercise-workout-fitness-centrum-man-woman-practicing-plank-gym_17801349.htm">Freepik</a>
  Photo by: <a href= "https://www.freepik.com/author/weyo">Weyo</a>
- [crossfit-image](assets/images/crossfitsmall.jpg): <a href="https://unsplash.com/photos/h3D-RRvxfqE">Unsplash</a>
  Photo by: <a href="https://unsplash.com/@bastien_plu">Bastien Plu</a>
- [trainer-image](assets/images/trainer.jpeg): <a href="https://www.pexels.com/photo/ethnic-woman-exercising-with-battling-ropes-near-male-trainer-6455771/">Pexels</a>
  photo by: <a href= "https://www.pexels.com/@julia-larson/">Julian Larson</a>

### Code

## Acknowledgements

- Tanks and acknowlegement goes to my mentor Mo Shami great guidance.
- Acknowledge my brother Addan Mc Collin for support form a user's veiw
- Thanks to my girlfriend Hiba Salem for support and input on a user veiw
- Thankful to the Slac
