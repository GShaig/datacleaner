=====
Data Cleaner
=====

DataCleaner is a data cleaning app built in Python by Shaig Gafarli. The App to be used to clean your dirty or raw data.

Using instructions: You first need to sign up to the service with your email address. Then you will be able to send your data file to the app and in seconds, the cleaned version will be supplied. After you're done, you can logout by clicking on 'Sign Out' button. This will direct you to the home page.

Used Python libraries: Pandas, django-allauth, Waitress, django-storages

Django framework was used to develop this app. Back-end: Python; Storage: AWS S3; Front-end: HTML & CSS

Quick start
-----------

1. Add "datacleaner" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'datacleaner.apps.DatacleanerConfig',
    ]

2. Include the datacleaner URLconf in your project urls.py like this::

    path('', include('datacleaner.urls')),

3. Run ``python manage.py migrate`` to create the datacleaner models.

4. The App uses AWS S3 storage. If you wish to use your S3 storage, you will need to put your S3 credentials into the settings.py file. Or, you can use your own storage.

5. Start the development server and visit http://127.0.0.1:8000/admin
   for admin interface (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/ to clean your data!

DataCleaner App is deployed to Heroku. Please visit https://datacleanser.herokuapp.com/
