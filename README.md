# what-i-watched
Django application to record what I wathced


## Starting from the Terminal

##install mysql python to support django with mysql
sudo apt-get install python-mysqldb

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver $IP:$PORT
    
## Configuration

You can configure your Python version and `PYTHONPATH` used in
Cloud9 > Preferences > Project Settings > Language Support.

## Support & Documentation

Django docs can be found at https://www.djangoproject.com/

You may also want to follow the Django tutorial to create your first application:
https://docs.djangoproject.com/en/1.9/intro/tutorial01/

Visit http://docs.c9.io for support, or to learn more about using Cloud9 IDE.
To watch some training videos, visit http://www.youtube.com/user/c9ide

Let’s say you created a Django app and ran python manage.py syncdb and created its table. Everytime you make a change in the table, you’ll need to drop that table and run syncdb again to update. And how you drop a table of a Django app:

    $ python manage.py sqlclear app_name | python manage.py dbshell

Drop tables of an app with migrations (Django >= 1.8):

    $ python manage.py migrate appname zero

Recreate all the tables:

    $ python manage.py syncdb

douban_id
26259677
