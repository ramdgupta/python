Virtual Environmentp
python3 -m venv .venv
.venv\Scripts\activate

Django installation
pip install Django

django-admin startproject myDjango
 cd myDjango
 python manage.py runserver


 Django Architechture
    uert > request> urls.py> view.py
    create views.py to call template or html page or text  and views.py always with this name only
    create template folder and static folder in parent dir
    settings.py TEMPLATES  'DIRS': ['templates'],
    to get resourse call {% load static %} in html at top
    for static resourses css and js import os  module and give setting beloww option in settingfile 
    STATIC_URL = 'static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

The outer mysite/ root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.
The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).
mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
mysite/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
mysite/asgi.py: An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with ASGI for more details.
mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.