=====
Data Cleaner
=====

Data Cleaner is a Django app to be used to clean your dirty or raw data. You first need to sign up to the service with your email address. Then you will be able to send your data file to the app and in seconds, the cleaned version will be supplied.

Detailed documentation is in the "docs" directory.

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

4. Start the development server and visit http://127.0.0.1:8000/admin
   for admin interface (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/ to clean your data!