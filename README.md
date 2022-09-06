# Prints by Futuro Berg

This E-commerce site, for the E-commerce Full Stack Project from Code Institute, consists of selling prints from professional analog photography made by Futuro Berg around the world. Each print has four different combinations for the user to choose, two different sizes and two different types of paper. The price of the print will depend and vary by the size of it that the customer chooses only and all the prints have the same price for each size. The user is able to buy both logged in and without registering the site, as a benefit of registering and login in the user will have a profile app that will give access to all past orders, also in the profile app the user will be able to update and save the delivery address information.

[Here is the live version of my project](https://prints-by-futuro-berg.herokuapp.com/)

![Welcome image](/assets/readme-images/first-run.png)

## Business Model and Planning

### Strategy Plane

#### Project Goals

- Create a full Stack e-commerce project with payment, authentication, different prints and different specs or attributes per print.
- B2C type of e-commerce offering prints to direct customers.
- Give the owner of the store the ability to manage the store both in the back end and the front end. 

#### External User's goal and Target Audience

- Users have the possibility to select a desired print with desired size and paper type, and also have the possibility to register in the e-commerce for order purchase history and easier delivery address information management.
- Enthusiastic people about professional analog photography.

#### Site owner's goals

- Futuro Berg wants a platform where he can show his art online and also be able to monetize from it.

### Scope Plane

#### Agile Methodology, Epics, User Stories and Tasks

##### Epic 1: Registration and User Accounts

1. Register an account:
    - As a site user I can register an account so that I will be able to view my profile and have a personal account.
        - Registration and account management with Allauth.
        - Profile app for the user to review past purchases and personal information.

2. Login and Logout:
    - As a site user I can login and logout from my account so that I can have access to my personal information.
        - Account management with Allauth working.
        - Manual testing with super user and normal user to check functionality.

3. Password recovery:
    - As a site user I can recover my password in case I forget it so that I can have access to my personal information again.
        - Account management with Allauth working.
        - Manual testing with super user and normal user to check functionality.

4. Account registration:
    - As a site user I can receive a confirmation via email from my account registration so that I can know that it was successfully created.
        - Account management with Allauth working.
        - Manual testing with super user and normal user to check functionality.

##### Epic 2: Viewing and Navigating

5. Prints list:
    - As a site user and customer I can view different prints so I can select some to purchase.
        - Create models, views and urls for products.
        - Manual testing that the prints are shown.

6. Prints details:
    - As a site user and customer I can see the information and details of each print so that I can see the description, rating, price, different images, choose size and type of paper.
        - Create product specs models, views and urls.
        - Manual testing that the prints specs are shown.

7. Messages for users:
    - As a site user and customer I can see messages so that I can know and have feedback of my interaction with the site.
        - Create toast for messages.
        - Manual Test that messages work.

8. Add print:
    - As the store owner I can add a print to the store so that the customers can buy it.
        - Add both possibilities to add prints in back and front end.
        - Manual testing both in front and back end.

9. Edit/update print:
    - As the store owner I can edit/update the information of a print so that I can change the price, description, images, size and paper type.
        - Allow deletion of prints in back end and front end.
        - Manual testing both in front and back end.

10. Delete prints:
    - As a store owner I can delete a print so that I can remove the ones that are no longer available for sale.
        - Allow deletion of prints in back end and front end.
        - Manual testing.

##### Epic 3: Sorting and Searching


11. Sort prints:
    - As a site user and custumor I can sort the prints by category so that I can easily choose the print I want.
        - Sort option available in the menu around the whole site.
        - Manual testing for the different categories.

12. Search Engine:
    - As a site user and customer I can search prints by description or name so I can choose the type of print I want.
        - Search bar available in the menu around the whole site.
        - Manual testing for name and description.

##### Epic 4: Purchasing and Checkout

13. Custom user profile:
    - As a site user I can have a personalised user profile so that I can review my purchase history, order confirmations and save my address and payment information.
        - Create models, views and urls for profile app.
        - Manual testing after checkout to see if everything works.

14. Total cart price:
    - As a site user and customer I can see the total amount of my prints in the cart so that I know how much I'm about to spend.
        - Cart icon available through the site.
        - Manual testing to check the correct price shown.

15. Print type selection:
    - As a site user and customer I can select the print, its size and paper type so that I'm sure I'm selecting what I really want.
        - Models, views, urls and jquery for showing different options to users.
        - Manual testing for these options to work.

16. View prints in cart:
    - As a site user and customer I can view my prints selections in my cart so that I can see the total amount of the future purchase and all the prints which I'll get.
        - Complete detail of quantity and print selection.
        - Manual testing all the information shown.

17. Modify cart:
    - As a site user and customer I can modify the quantity of different prints in my cart, so that I can modify my final purchase before the checkout.
        - Change quantity of selected print or delete a selected print from the cart.
        - Manual testing for both options working.

18. Payment information:
    - As a site user and customer I can easily enter my payment details so that I can easily checkout and finish my purchase.
        - Fluid connection between prints details, cart and check out.
        - Manual testing.

19. Checkout security:
    - As a site user and customer I can search prints by description or name so I can choose the type of print I want.
        - External card validator with Stripe.
        - Webhooks for double insurance that the payments get processed correctly.

20. Order confirmation:
    - As a site user and customer I can view an order confirmation after making the purchase so that I can see that the purchase is done with any mistake.
        - Pop up message confirmation.
        - Checkout page with order details.

21. Confirmation email:
    - As a site user and customer I can receive an email with my purchase confirmation and information so that I can have a record of what I've purchased
        - Pop up message confirmation with customer email.
        - Manual check.


### [Agile Methodology used to accomplish the goals from the project via User Stories](https://github.com/users/matiasconsiglio/projects/1)

### Scope Plane

![Entity Relationship Diagram](/assets/readme-images/entity-relationship-diagram.png)

- Entity relationship diagram for relational databse schema
    - This image shows the process, communication between apps and models to be able to accomplish the scope goals and accept the different tasks for all de user stories and their epics. 
    - For this project "improvisation" was required in terms of coding, since to offer the option of different sizes and different types of paper for the same product/print, three new models were created in the beginning beyond category and product model. Product specs model, size mode and paper model and they connect as shown in the image. To connect these models to the bag app, Jquery is needed to manage the different option inputs from users from the front end connecting to the back end thanks to context.py from the bag app.
    - From the other side, the User model that comes with Allauth is connected to UserProfile model from the profile app, this will allow the logged user to see, review order history and manage delivery address information.
    - Order model is connected to user profile, this model allows anyway to sell to users not registered, and finally connected to OrderlineItem from checkout the app with the order number generated and all the details from the user.
    - Interesting connection of all the models, views, functions and apps occurs in the model orderLineItem from checkout app. One that takes the information from the items being bought from bag_contents, especifically bag_items, that includes all the needed information to make a correct sale, with the correct item details, prices, types and at the same time with the order generated with the customer details. 

### Skeleton Plane

- Diagram for UX design

![Diagram for Ux Design](/assets/readme-images/diagram.png)

- Mock-up

![Mock-up for Ux Design](/assets/readme-images/mock-up-1.png)

![Mock-up for Ux Design](/assets/readme-images/mock-up-2.png)

![Mock-up for Ux Design](/assets/readme-images/mock-up-3.png)

![Mock-up for Ux Design](/assets/readme-images/mock-up-4.png)

![Mock-up for Ux Design](/assets/readme-images/mock-up-5.png)

![Mock-up for Ux Design](/assets/readme-images/mock-up-6.png)

![Mock-up for Ux Design](/assets/readme-images/mock-up-7.png)

![Mock-up for Ux Design](/assets/readme-images/mock-up-8.png) 

- All the special pages for login, register, logout and update comment should share the same navbar and footer as the main view.

### Surface Plane

- Images were taken and given permission to use from the professoinal photographer Futuro Berg. All the prints and background are part of his talented job, so to make it more interesting for the view for users, a greyish tone of colors were used in the webpage giving space and attention to the prints themself in sale.

## Features

### Existing Features Tested Manually and Messages for User

-  Welcomes the user to the e-commerce "Prints" by Futuro Berg.

    - Has a Logo with a link to the home page.
    - Has a register and login option for the user in the navbar.
    - Has a link to Futuro's principal webpage.
    - Has the biography of Futuro Berg.
    - Has a button to shop prints.
    - Has a search bar to search for print names or description.
    - Has a expandable Print option to sort prints by category or by all prints.
    - Has a bag/cart icon that redirects the user to the shopping bag with the items added until the moment.
    - Has a text promotion for free delivery.
    - Has a footer with link to facebook page for marketing, privacy policy and subscribe option to the site newsletter.

![First blog approach](/assets/readme-images/first-run.png)

Home page approach.

- Register for User.

    - Special design page that allows the user to register to Prints.
    - Explanation to the user in case they already have and account, button option to go to sign in page.
    - Username, password and password confirmation required.
    - User email double input.
    - Sign up button for confirmation.
    - Messages shown in case the name of the user or email already exists.
    - Successfull message for correct registration asking for activate account.
    - Successfull redirect of page for correct registration asking for activate account.
    - Redirect to Sign In after email verification.
    - Navbar and footer keeps the style of the welcome page.

 
![Registration](/assets/readme-images/register.png)

Register page with link to sign in page.

![Registration success](/assets/readme-images/register-success.png)

Verification page after register.

![Registration email](/assets/readme-images/email.png)

Email confirmation

![Registration email verification](/assets/readme-images/email-verification.png)

Email verification link.

![Registration account verified](/assets/readme-images/account-verified.png)

Account verified

![Registration](/assets/readme-images/user-exist.png)

User name and/or email message already exist.

- Login for User.

    - Special design page that allows the user to Login to Prints.
    - User and Password required.
    - Remember me checkbox.
    - Sign in button.
    - Message shown in case the username or password is incorrect.
    - Navbar and footer keeps the style of the welcome page.
    - Link that allows you to go to the register page in case you don't have an account created.
    - Forgot password link and email for password recovery.

![Login](/assets/readme-images/account-verified.png)

Login Page with message and link for register.

![Incorrect login](/assets/readme-images/incorrect-login.png)

Incorrect login. 

![Password reset](/assets/readme-images/password-reset.png)

Password reset.

![Password reset email sent](/assets/readme-images/password-reset-email.png)

Password reset email sent.

![Change password](/assets/readme-images/change-password.png)

Change password.

![Password changed](/assets/readme-images/password-changed.png)

Password changed.

- Logout

    - Logout message asking the user if it is sure they want to logout.
    - Sign out button.
    - Navbar and footer keeps the style of welcome page.
    - Once Sign Out is clicked the user is redirected to the home page.

![Sign in confirmation](/assets/readme-images/sign-in-confirmation.png)

Sign in confirmation

![Logout](/assets/readme-images/log-out.png)

Log out page.

![Logout confirmation](/assets/readme-images/log-out-confirmation.png)

Redirect to home after sign out and logout confirmation.

- Prints page

    - Prints available.
    - Name, description and category
    - Navbar and footer keeps the style of the welcome page.

    - If super user, edit and delete print available options in prints and navbar.
 
![Prints](/assets/readme-images/prints.png)

Prints view.

![Prints view for super user](/assets/readme-images/prints-super.png)

Prints view for super user.

![Add print](/assets/readme-images/add-print.png)

Add print.

![Add print success](/assets/readme-images/add-success.png)

Add print success.

![Add print specs](/assets/readme-images/spec.png)

Add print specs.

![Add print specs type](/assets/readme-images/choose-spec.png)

Add print specs type.

![Add print specs type success](/assets/readme-images/spec-success.png)

Add print specs type success.

![Added print view](/assets/readme-images/new-print-view.png)

Added print view.

![Added print spec view](/assets/readme-images/spec-view.png)

Added print specs view.

![Delete print](/assets/readme-images/delete.png)

Deleted print message.

![Media require](/assets/readme-images/media-require.png)

Media require for adding print.

![Print added in admin](/assets/readme-images/product-admin.png)

Print added in admin.

![Print added in admin destription](/assets/readme-images/admin-att.png)

Print added in admin description.

![Print added in admin specs](/assets/readme-images/admin-spec.png)

Print added in admin specs.

- Print details
    - Name.
    - Description.
    - Paper size options.
    - Paper type options.
    - Price.
    - Quantity selector.
    - Add to cart.
    - Keep shopping.

![Print added to cart plus pop-up cart message](/assets/readme-images/print-detail-cart.png)

Print added to cart plus pop-up cart message.

- Purchasing example
    - Log in with natural user.
    - Order by category.
    - Search for prints.
    - View bag.
    - Checkout.
    - Webhooks. 
    - Order confirmation.
    - Check order in the profile view for loged in users.

- Admin models
    - Size.
    - Paper.
    - Category.
    - Product.
    - ProductSpec.
    - 

- Marketing
    - Facebook page created for marketing purpose.
    - [Facebook page](https://www.facebook.com/FuturoBergPrints/)

![Marketing cover](/assets/readme-images/marketing-1.png)

Marketing cover.

![Marketing profile picture](/assets/readme-images/marketing-2.png)

Marketing profile picture

![Marketing first post](/assets/readme-images/marketing-3.png)

Marketing first post.

![Marketing shop button](/assets/readme-images/marketing-4.png)

Marketing shop button

![Marketing over-view](/assets/readme-images/marketing-5.png)

Marketing over-view

![Marketing over-view](/assets/readme-images/marketing-7.png)

Marketing link in footer

- Privacy policy

![Marketing over-view](/assets/readme-images/marketing-7.png)

Privacy policy link

![Marketing over-view](/assets/readme-images/privacy.png)

Privacy policy 

- SEO
    - Metatags used with keywords selected upon search data in the web. robot.txt file created with sitemap.xml to help the search optimization of Prints webpage in google. Also spans, and strong attributes were used in important places and keywords through the code. The following images are examples of all the implementation of SEO in the project.

![SEO Span and Strong](/assets/readme-images/seo-1.png)

Span and strong used.

![SEO Span and Strong](/assets/readme-images/seo-2.png)

Span and strong used.

![SEO Span and Strong](/assets/readme-images/seo-3.png)

Span and strong used.

![SEO Keyword selection for metatag](/assets/readme-images/seo-4.png)

Keyword selection for metatag.

![SEO Keyword selection for metatag](/assets/readme-images/seo-5.png)

Keyword selection for metatag.

![SEO Keyword selection for metatag](/assets/readme-images/seo-6.png)

Keyword selection for metatag.

![SEO Keyword selection for metatag](/assets/readme-images/seo-7.png)

Keyword selection for metatag.

![SEO Keyword selection for metatag](/assets/readme-images/seo-8.png)

Keyword selection for metatag.

![SEO Correct use of Alt attribute and use of external important webpage](/assets/readme-images/seo-9.png)

Correct use of Alt attribute and use of external important webpage.

![SEO robots.txt](/assets/readme-images/seo-11.png)

robots.txt

![SEO sitemap.xml](/assets/readme-images/seo-12.png)

sitemap.xml    

- Security
    - All environmental variables were connected in "Config Vars" in heroku, safe and secure place.
        - AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, DATABASE_URL, EMAIL_HOST_PASS, EMAIL_HOST_USER, SECRET_KEY, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY and USE_AWS.


## Features Left to Implement

- Allow super user to update and delete Specs from Prints in the front end.
- Allow users to login with social-media platforms like "Gmail" or "Facebook".
- Fix and update delivery options with companies like "DHL" or "PostNord".

### Bugs

- If the super user decides to add a print and after add specs to it, if the super user doesn't follow the message explaining the order of each spec to be added in the front end, after when a user will try to make an order, the information will not appear correctly in the cart. This bug has a deep jquery connection, that has to be followed and at the same time needs new knowledge beyond the course to be able to fix it. If the super user follows the order mention everything would works properly. Other option would be to generate 4 different forms where the super user only chooses the price inside the product spec model per print option. 

- After final deployment, error h10 was showed and the heroku app was crushing. With help of tutor session, bug was fixed changing Procfile with "prints" instead of "prints-by-futuro-berg".

- Error 500 after deployment when trying to generate new user. STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), ) changed to STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]. First one is the one used in the last version of Boutique Ado.


## Deployment

- The site was deployed to heroku.com using Code Institute's mock terminal for Heroku. For this it is needed to install Django and supporting libraries, create a new blank Django project and app, set the project to use Stripe and PostgreSQL and deploy to heroku.

Deployment to heroku:

1. Create new App in heroku.
2. In resources add-on Postgres.
3. "pip3 install dj_database_url" in gitpod terminal.
4. "pip3 install psycopg2-binary" in gitpod ternminal.
5. "pip3 freeze > requirements.txt" in gitpod terminal.
6. In setting.py "import dj_databse_url".
7. In settings.py add:
	
if "DATABASE_URL" in os.environ:

    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

8. In heroku in settings in config vars find the DATABE_URL then add it in env.py and gitpod variables.
9. "pip3 install django-allauth==0.51.0" in gitpod terminal to fix problem of compatibility of allauth, python and stripe versions.
10. "python3 manage.py makemigrations" in gitpod terminal.
11. "python3 manage.py migrate" in gitpod terminal.
12. Transfer data from sql to postgres via json file.
	
#if "DATABASE_URL" in os.environ:

    #DATABASES = {
        #"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
    #}
#else:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

12. "python3 manage.py dumpdata products > products.json" in gitpod terminal.
13. In settings.py :
	
if "DATABASE_URL" in os.environ:

    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

14. "python3 manage.py loaddata products.json" in gitpod terminal.
15. Create super user "python3 manage.py createsuperuser" in gitpod terminal.
16. "pip3 install gunicorn" in gitpod terminal.
17. "pip3 freeze > requirements.txt" in gitpod terminal.
18. Create Procfile "web: gunicorn prints.wsgi:application".
19. Heroku login Github terminal command: "heroku login -i".
20. "heroku git:remote -a prints-by-futuro-berg" in gitpod terminal.
21. "heroku config:set DISABLE_COLLECTSTATIC=1" in gitpod terminal.
22. In settings.py 
	
ALLOWED_HOSTS = ['prints-by-futuro-berg.herokuapp.com', 'localhost']

23. Create a runtime.txt with python-3.9.13 inside
24. "git add ." , 'git commit -m "Deployment 1"', "git push" and "git push heroku main" in gitpod terminal.
25. In heroku, Deploy, Deployment method, connect to github, repository name: matias, prints and connect, emable automatic deploy.
26. Django secret key generator, add it in config vars in heroku. In settings.py 
	SECRET_KEY = os.environ.get('SECRET_KEY', '')
27. "DEBUG = 'DEPLOYMENT'" in os.environ.
28. "git add ." , 'git commit -m "Deployment 2"', "git push" and "git push heroku main" in gitpod terminal.
29. Navigate to aws.amazon.com and create account.
30. Create bucket in S3, object ownership with ACLs enabled and bucket owner prefered. Defined public. Static website hosting in properties enable and index.html error.html.
31. Permissions:

[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]

32. Policy tab, Policy generator with Select Type of Policy: S3 Bucket Policy.
33. Allow all principal with "*".
34. Action "get object".
35. ARN ":arn:aws:s3:::prints-by-futuro-berg".
36. Add statement and generate policy, copy and past in bucket policy adding /* at the end of "Resource".
37. For the Access control list (ACL) section, click edit and enable List for Everyone (public access) and accept the warning box.
38. Back in Services menu, open "IAM".
39. In User groups create group, create name, create group.
40. in User groups in policies, create policy.
41. In jason tab, import managed policy, choose "AmazonS3FullAccess".
42. Add in "JSON Policy":

"Resource": [
    "arn:aws:s3:::prints-by-futuro-berg*",
    "arn:aws:s3:::prints-by-futuro-berg/*"
]

43. In review policy choose name and description, create policy.
44. To attach the policy, on the sidebar click User Groups. Select your group, go to the permissions tab, open the Add permissions dropdown, and click Attach policies. Select the policy and click Add permissions at the bottom.
45. In Users, add user, select name ad programmatic access.
46. Add user to group then create user.
47. Download .csv file.
48. "pip3 install boto3" in gitpod terminal.
49. "pip3 install django-storages" in gitpod terminal.
50. "pip3 freeze > requirements.txt"
51. Add storages to installed apps in settings.py.
52. In settings.py:
	
if 'USE_AWS' in os.environ:

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'prints-by-futuro-berg'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

53. Add keys to config var in heroku (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KE (both get from .csv downloaded) and "USE_AWS = True".
54. Create custom_storages.py.
55. Add on custom_storages.py:

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
    
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION

56. In settings.py:

 
if 'USE_AWS' in os.environ:
	
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
	
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'prints-by-futuro-berg'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.envßiron.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

57. "git push" in gitpod terminal.
58. In S3 create new folder called media, upload media granting public read access to objects, then upload.
59. Add stripe key to heroku config variables (publishable key in API keys and secret key) "STRIPE_PUBLIC_KEY" and "STRIPE_SECRET_KEY".
60. In Webhooks, add end point url: "https://prints-by-futuro-berg.herokuapp.com/checkout/wh/" select all events.
61. Add webhook signing secret to config vars in heroku "STRIPE_WH_KEY".



## PEP8 and HTML, CSS validators and lighthouse

### PEP8

- events/admin.py
![PEP8 events admin.py](/assets/readme-images/pep8-adminpy.png)

- events/apps.py
![PEP8 events apps.py](/assets/readme-images/pep8-appspy.png)

- events/forms.py
![PEP8 events forms.py](/assets/readme-images/pep8-formspy.png)

- events/models.py
![PEP8 events models.py](/assets/readme-images/pep8-modelspy.png)

- events/urls.py
![PEP8 events urls.py](/assets/readme-images/pep8-urlspy.png)

- events/views.py
![PEP8 events views.py](/assets/readme-images/pep8-views.png)

- subtevents/asgy.py
![PEP8 subtevents asgy.py](/assets/readme-images/pep8-asgi.png)

- subtevents/settings.py
![PEP8 subtevents settings.py](/assets/readme-images/pep8-settingspy.png)

- subtevents/urls.py
![PEP8 subtevents urls.py](/assets/readme-images/pep8-urls2py.png)

- subtevents/wsgi.py
![PEP8 subtevents wsgi.py](/assets/readme-images/pep8-wsgipy.png)

- manage.py
![PEP8 manage.py](/assets/readme-images/pep8-managepy.png)

### W3C CSS

- CSS
![W3C CSS Validator](/assets/readme-images/w3c-css.png)

### W3C HTML

- HTML
![W3C HTML Validator](/assets/readme-images/html-validator.png)

- Lighthouse
![Developers lighthouse](/assets/readme-images/lighthouse.png)


## Dependencies, frameworks, languages and django packages used

- Code Institute template used for ability to deploy the program correctly in Heroku.
- HTML and Bootsrap, CSS, DJANGO, PYTHON, Javascript and Jquery.
- Config Vars: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY and USE_AWS for static and images files connected with amazon web services S3 bucket,  value = 8000 improve compatibility with various Python libraries in heroku, import dj_database_url for DATABASE_URL environment variable to configure your Django database configuration with heroku application. STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY for connecting stripe payments. Finally SECRET_KEY. All environment variables where added to heroku config vars (secure location).
- Stripe webhooks for allowing the site to make correct orders in case something happens when the user press "checkout" and the payment is processed, also workd as indicator for evey movement related to stripe. Super user can use this for understanding the status of stripe connection with the e-commerce.
- Gunicorn for heroku server, Crispy forms for comments section, Allauth for user registration and Login/Loggout, Psycopg2 connect PostgreSQL with Python. 
- Git for coding commit and pushing to Github, Github for project code repository store, Heroku python deployment to web, PostgreSQL database.
- Uizard for mock-up creation.
- Onenote for Flow diagram.
- Github projects for agile metodology.
- Facebook page for marketing, mailchimp for mail subscription.
- Requirements.txt with:

    - asgiref==3.5.2
    - backports.zoneinfo==0.2.1
    - boto3==1.24.66
    - botocore==1.27.66
    - dj-database-url==1.0.0
    - Django==4.1
    - django-allauth==0.51.0
    - django-countries==7.2.1
    - django-crispy-forms==1.14.0
    - django-storages==1.13.1
    - gunicorn==20.1.0
    - jmespath==1.0.1
    - oauthlib==3.2.0
    - Pillow==9.2.0
    - psycopg2-binary==2.9.3
    - PyJWT==2.4.0
    - python3-openid==3.2.0
    - pytz==2022.1
    - requests-oauthlib==1.3.1
    - s3transfer==0.6.0
    - sqlparse==0.4.2
    - stripe==4.1.0


## Credits

- All code was done by the student with the support of Code Institute classes, following "Boutique ado" project construction adaptation for Prints.

- Models where managed and built by the help of the student mentor and [Code Artisan Lab](https://github.com/codeartisanlab) with ecommerce-website-in-django-3-and-bootstrap-4 project, specifically the option to choose different sizes and paper type. 

- Code Institute Slack comunity for checking errors and getting info from people that had already discuss the subject.

- All Media content was uploaded by the student and done by Futuro Berg, professional photographer.

- Code Institute and heroku for deployment terminal.
