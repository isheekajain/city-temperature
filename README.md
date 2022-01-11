City Temperature
=========================
 
 ### Table of Contents  
[Description](#desc)  
[Features](#features) 
[Setup](#setup)

Description
===========
city-temperature is a web application built with Django that fetches temperature from the Open Weather Map API and then sends an email providing the temperature of particular city.

<a name="features"/>
Features
========
* Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
* Enhancements to Django's static file serving functionality via WhiteNoise.
* Latest Python 3.6 runtime environment.
* Configure SMTP servers.

<a name="setup"/>
Setup
=====
> NOTE: 1. Add your `API_KEY` in `views.py` that you can generate from (https://openweathermap.org/api)
>2. Add your email and password in `settings.py`
1. cd into the repository location in your machine.
2. Run the requrements `$ pip install -r requirements.txt`
3. Migrations `$ python manage.py migrate`
4. Run the server `$ python manage.py runserver`


