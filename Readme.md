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



**15-June-2022**

Create two folders static and templates in app folder.
static for css and js files
templates for html


create a urls.py file inside app


Create templates and static folder in app
>css js images in static
>html etc in templates

create a urls.py file inside app

connect created url file with project's url file
>path('',include('myapp.urls'))

inside app's urls.py
>from django.urls import path
>urlpatterns=[path('',index,name="index")]
>index function will be made in views.py
Note index function will be called when given path is entered in browser in case path is ''
index function will be inside views.py




create another html inside app and add it to urls.py under name 'next'
link it with first page.
