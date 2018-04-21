# The things

A Craigslist-like application built with Django.

## Python virtualenv

I would recommend you to use a virtualenv.

To create it use the following command:
```
virtualenv --python=[path to python 3.5.1] myenv
```
Do not forget to include pip.

Then to activate it execute the activate script use :
```
./myenv/Scripts/activate
```
on windows or
```
./myenv/bin/activate
```
on Posix.

If you want to deactivate the virtualenv just use the following command:
```
deactivate
```

## Install Required Packages
First of all you have to install the mendatory libraries. To install them use the following command:

```
pip install -r requirements.txt
```

## Running the Application
Before running the application you will need to create the needed DB tables:
```
python ./manage.py migrate
```
Now you can run the development web server:
```
python ./manage.py runserver
```
To access the applications go to the URL http://localhost:8000/


## Manage the website
If you want you can create a superuser.
```
python ./manage.py createsuperuser
```
