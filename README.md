# Django Framework Tutorial

This repo contains my personal notes while following a YT tutorial on Django.

[source](https://www.youtube.com/watch?v=F5mRW0jo-U4)

[Github repo](https://github.com/codingforentrepreneurs/Try-Django)

## Setup

**Virtual environment**

Install pip: `sudo apt-get install python3-pip`

Install virtualenv using pip3: `sudo pip3 install virtualenv`

Create a virtual environment: `virtualenv venv`

Create virtualenv using Python3: `virtualenv -p python3 myenv`

Or: `virtualenv -p python3 .`

Use a Python interpreter of your choice: `virtualenv -p /usr/bin/python2.7 venv`

Activate your virtual environment: `source venv/bin/activate`

To deactivate: `deactivate`

**Django**

`pip install django==2.0.7`

To show installed libraries: `pip freeze`

`django-admin`

`django-admin startproject trydjango .`

**Setup Text Editor**

## Settings

`settings.py`

`python manage.py migrate`: syncs our settings

`python manage.py createsuperuser`

**Your First App Component**

`python manage.py startapp products`

`models.py`:

```python
# Create your models here.
class Product(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
```

`settings.py`:

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party

    # own
    'products',
]
```

`python manage.py makemigrations`

`python manage.py migrate`

`products/admin.py`:

```py
from .models import Product

admin.site.register(Product)
```

