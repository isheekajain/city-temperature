City Temperature
=========================
 
 
Description
===========
city-temperature is a web application built with Django that fetches temperature from the Open Weather Map API and then sends an email providing the temperature of particular city.

Features
========
* Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
* Enhancements to Django's static file serving functionality via WhiteNoise.
* Latest Python 3.6 runtime environment.
* Configure SMTP servers.

Setup
=====
1. cd into the repository location in your machine.
2. Run the requrements `$ pip install -r requirements.txt`
3. Migrations `$ python manage.py migrate`
4. Run the server $ python manage.py runserver
