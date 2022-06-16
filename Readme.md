--------------------------------------------------------------------
--------------------------------------------------------------------
**14-June-2022**
Creating a Project
> django-admin startproject mysite


Create app
>django-admin startapp projectApp
or
>python manage.py startapp projectApp
Note: Can have multiple apps in a project and one app in multiple projects.



Creating a SuperUser
>python manage.py createsuperuser
Note: can also add user by server-url/admin



Create default (sql)tables for installed apps
>python manage.py migrate 


Run django server
>python manage.py runserver


Add app in project
>goto settings.py and append name of created apps in INSTALLED_APPS List