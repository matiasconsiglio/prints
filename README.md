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

- Users have the possibility to select a desired print with desired size and paper type, also have the possibility to register in the e-commerce for order purchase history and easier delivery address information management.
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

3. Approve Comments.
    - As a an Admin I can approve or disapprove comments so that I can filter out objectionable comments.

4. Site Pagination:
    - As a Site User I can view a paginated list of events so that I can easily select a post to view.

5. View Event List:
    - As a Site User I can view a list of events so that I can select one to watch and read.

6. View Likes:
    - As a Site User / Admin I can view the number of likes in each event so that I can see which one is more popular.

7. View Comments:
    - As a Site User / Admin I can view comments on an individual event so that I can read the conversation.

8. Open an Event:
    - As a Site User I can click on an event so that I can see all the information and media from it.

9. Account Registration:
    - As a Site User I can register an account so that I can comment and like different events.

10. Comment on an Event:
    - As a Site User I can comment on an event so that I can interact with it.

11. Edit and Delete Comments:
    - As a Site User I can choose to manipulate my comment so that I can edit it or delete it.

12. Like and Unlike Events:
    - As a Site User I can like or unlike an event so that I can interact with the content.

13. Social Media:
    - As a Site User I can interact with the event social media so that I can follow the different DJs and/or organisers.

14. View Media from Events:
    - As a Site User I can see and/or listen to different media from the event so that I can understand and feel how the event was.

### [Agile Methodology used to accomplish the goals from the project via User Stories](https://github.com/matiasconsiglio/project-4/projects/1)

### Diagram for UX design

![Diagram for Ux Design](/assets/readme-images/diagram.png)

- All the special pages for login, register, logout and update comment should share the same navbar and footer as the main view.

## Features

### Existing Features Tested Manually and Messages for User

-  Welcomes the user to the events blog "ΠΛΤΤ Sessions".

    - Has a Logo with a link to the home page.
    - Has a register and login option for the user in the navbar.
    - Has a Home link to the home page.
    - Shows the different events that have already happened and the ones to come.
    - Shows the different likes each event has.
    - Allows the user to click on "Session #number" to go inside each event and see different information and media from it.
    - Show the social media from ΠΛΤΤ Sessions for users to be able to reach and follow.
    - In case the user is logged in, the navbar won't show register and login, instead will show the option Logout.

![First blog approach](/assets/readme-images/first-run.png)

First blog approach.


![Blog Logout](/assets/readme-images/first-run-logout.png)

Blog log out option and message.


- Register for User.

    - Special design page that allows the user to register to ΠΛΤΤ Sessions.
    - Explanation to the user in case they already have and account, button option to go to sign in page.
    - Username, password and password confirmation required.
    - User email input as optional.
    - Sign up button for confirmation.
    - Messages shown in case the name of the user already exists.
    - Navbar and footer keeps the style of the welcome page.
    - Link that allows you to go to the sign in page in case you already have an account created.

 
![Registration](/assets/readme-images/register.png)

Register page with link to sign in page.


![User already exist](/assets/readme-images/user-exist.png)

User message already exist.


- Login for User.

    - Special design page that allows the user to Login to ΠΛΤΤ Sessions.
    - User and Password required
    - Remember me checkbox
    - Sign in button
    - Message shown in case the username or password is incorrect.
    - Navbar and footer keeps the style of the welcome page.
    - Link that allows you to go to the register page in case you don't have an account created.

![Login](/assets/readme-images/login.png)

Login Page with message and link for register.


![Incorrect login](/assets/readme-images/incorrect-login.png)

Incorrect login. 


- Logout

    - Logout message asking the user if it is sure they want to logout.
    - Sign out button.
    - Navbar and footer keeps the style of welcome page.
    - Once Sign Out is clicked the user is redirected to the home page.


![Logout](/assets/readme-images/logout.png)

Sign out confirmation page.


![Home](/assets/readme-images/first-run.png)

Redirect to home after sign out.


- Event

    - Number of likes and comments.
    - Possibility to see comments from different users.
    - Navbar and footer keeps the style of the welcome page.
    - Flyer of the event.

    - Depending on the event, the post can have:
        - None, one or more guest Djs.
        - Bio of different guest Djs.
        - Social Media from guest Djs.
        - Photos and embedded videos from Youtube and sound from Soundcloud.
        - ΠΛΤΤ media including photos, videos or/and audio.

    - For all events if the user is logged in:
        - Possibility to comment and wait for approval from Admin of the comment.
        - If the user already commented and the comment was approved; possibility of updating and/or deleting the same user comment.
        - Like the event.
 
![Event post intro plus like option](/assets/readme-images/session2-1.png)

Event first view liked by the user.


![Home page with like](/assets/readme-images/home-like.png)

Home page with like.


![Event guest dj video and audio](/assets/readme-images/session2-2.png)

Guest Dj media.


![Matt media 1](/assets/readme-images/mattmedia1.png)

ΠΛΤΤ media.


![Matt media 2](/assets/readme-images/mattmedia2.png)

ΠΛΤΤ media.


![Matt media 3](/assets/readme-images/mattmedia3.png)

ΠΛΤΤ media.


![Logged in comment view](/assets/readme-images/loggedin-comment-view.png)

Logged-in comment view.


![Logged in commented waiting for approval](/assets/readme-images/comment-view-waiting-approval.png)

Logged-in comment sent waiting for approval.


![Logged in comments view](/assets/readme-images/loggedin-comment-approved.png)

Logged-in comment section after approval.


![Logged out comment view](/assets/readme-images/logged-out-comment-view.png)

Logged-out comment section.


- Update comment.
    - Only available for logged in users and for updating their own users comment.
    - Sends you to another page to update and send your new comment
    - New comment needs approval.
    - Old comment gets deleted.

![Logged in comments view](/assets/readme-images/loggedin-comment-approved.png)

Logged-in comment section after approval.


![Update comment view](/assets/readme-images/update-comment.png)

Update comment view.


![Update comment waiting for approval](/assets/readme-images/update-comment-waiting-approval.png)

Update comment waiting for approval.


![Update comment view after approval](/assets/readme-images/update-comment-approved.png)

Update comment view after approval.


![Different user logged in comments view](/assets/readme-images/different-user-logged-comment-view.png)

Different user logged in comments view.

  
- Delete comment.
   - Only available for logged in users and for deleting their own comments.
   - Pop-up message with back and delete confirmation option.

![Delete in comments view](/assets/readme-images/delete-comment.png)

Delete in comments view logged in as author.


![Delete pop-up message confirmation](/assets/readme-images/delete-comment-pop-up.png)

Delete pop-up message confirmation.


![View after choosing back deleting](/assets/readme-images/delete-comment-back.png)

View after choosing back deleting.


![View after deleting comment](/assets/readme-images/deleted-comment.png)

View after deleting comment.


![Delete option view for different user than author](/assets/readme-images/delete-comment-other-user-logged-in.png)

Delete option view for different user than author of comment.


- Responsive on all device sizes and has interactive elements.

    - Web, Ipad Air and Iphone 12 pro.

![Welcome image](/assets/readme-images/first-run.png)

Web.


![Ipad Air view](/assets/readme-images/ipad-air.png)

Ipad.


![Iphone 12 pro view](/assets/readme-images/iphone-12-pro.png)

Iphone 12 pro.


![Navbar open menu](/assets/readme-images/iphone-12-pro-open-menu.png)

Navbar open menu.

- Admin Back-end

    - Allows the admin to do CRUD in the back-end of the site. with special effect in Comments and Events("Posts")

![Admin image](/assets/readme-images/admin.png)

Admin image.


![Admin Comments section](/assets/readme-images/admin-comment.png)

Admin Comments section.


![Admin Events section](/assets/readme-images/admin-event.png)

Admin Events section.


![Admin Events edit section](/assets/readme-images/admin-event-edit.png)


Admin Events edit section.


## Features Left to Implement

- Allow super user to update and delete Specs from Prints in the front end.
- Allow users to login with social-media platforms like "Gmail" or "Facebook".
- Fix and update delivery options with companies like "DHL" or "PostNord".

### Bugs

- If the super user decides to add a print and after add specs to it, if the super user doesn't follow the message explaining the order of each spec to be added in the front end, after when a user will try to make an order, the information will not appear correctly in the cart. This bug has a deep jquery connection, that has to be followed and at the same time needs new knowledge beyond the course to be able to fix it. If the super user follows the order mention everything would works properly. Other option would be to generate 4 different forms where the super user only chooses the price inside the product spec model per print option. 

- After final deployment, error h10 was showed and the heroku app was crushing. With help of tutor session, bug was fixed changing Procfile with "prints" instead of "prints-by-futuro-berg".


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
