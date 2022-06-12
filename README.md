# Django Framework Tutorial

This repo contains my personal notes while following a YT tutorial on Django.

[source](https://www.youtube.com/watch?v=F5mRW0jo-U4)

[Github repo](https://github.com/codingforentrepreneurs/Try-Django)

[API Reference](https://docs.djangoproject.com/en/2.0/ref/)

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

**Create Product Objects in the Python Shell**

`python manage.py shell`: imports your django project into a python shell

example: 

`from products.models import Product`

`Product.objects.all()`

`Product.objects.create(title="New product 2", description="new one", price="19292", summary="sweet")`

**New Models Fields**

[Field types docs](https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types)

```py
# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)  # max_length = required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=1000)
    summary     = models.TextField()
```

**Change a Model**

> Make a new change to the model without deleting the database

```py
# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)  # max_length = required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=1000)
    summary     = models.TextField()
    featured    = models.BooleanField()
```

`null=True`
`default=True`
`blank=True` -> required or not field

blank how the field is rendered, null means database entry can be empty

**Default Homepage to Custom Homepage**

> we do this by creating a class or function based view

`python manage.py startapp pages`

`views.py`: handles your various webpages

```py
from django.http import HttpResponse

# Create your views here.

def home_view(*args, **kwargs):
    return HttpResponse("<h1> Hello World </h1>")
```

`urls.py`:

```py
from pages import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view),
    path('admin/', admin.site.urls),
]
```

**URL Routing and Requests**

```py
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
```

Output:

```
() {}
<WSGIRequest: GET '/'>
```

`print(request.user)` will print the logged in user.

**Django Templates**

Create a new folder called `templates`; update `views.py` to return the requested page using:

```py
return render(request, "home.html", {})
```

In `settings.py`; indiciate the path to your template folder:

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
```

**Django Templating Engine Basics**

`base.html` template:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>
            Coding for Entrepreneurs
        </title>
    </head>
    <body>
        <h1>This is a navbar</h1>
        {% block content %}
            replace me
        {% endblock %}
    </body>
</html>
```

`home.html` template:

```html
{% extends 'base.html' %}

{% block content %}
<h1>Hello world</h1>
{{ request.user.is_authenticated }}
<p>This is a template</p>
{% endblock %}
```

**Include Template Tag**

Create a new `navbar.html` template:

```html
<nav>
    <ul>
        <li>Home</li>
        <li>Contact</li>
    </ul>
</nav>
```

Update `base.html`:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>
            Coding for Entrepreneurs
        </title>
    </head>
    <body>
        {% include 'navbar.html' %}
        {% block content %}
            replace me
        {% endblock %}
    </body>
</html>
```

**Rendering Context in a Template**

We can pass in context variables through the dictionary:

```
def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about me",
        "my_number": 123,
        "my_list": [123, 345]
    }
    return render(request, "contact.html", my_context)
```

And display them like this:

```
<p>
    {{ my_text }}, {{ my_number }}, {{ my_list }}
</p>
```

**For Loop in a Template**

Iterate trough list inside html code:

```html
<ul>
    {% for my_sub_item in my_list %}
    <li>{{my_sub_item}}</li>
    {% endfor %}
</ul>
```

**Using Conditions in a Template**

```html
{% for my_sub_item in my_list %}
    {% if my_sub_item == 312 %}
        <li>{{ forloop.counter }} - {{ my_sub_item|add:22 }}</li>
    {% elif my_sub_item == 123 %}
        <li>Custom message</li>
    {% else %}
    <li>{{ forloop.counter }} - {{my_sub_item}}</li>
    {% endif %}
{% endfor %}
```

**Template Tags and Filters**

[Template Tags reference](https://docs.djangoproject.com/en/2.0/ref/templates/builtins/)

[Built-in filter reference](https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#built-in-filter-reference)

**Render Data from the Database with a Model**

1:49:19

Open Python shell: python manage.py shell

>> from products.models import Product
>> Product.objects.get(id=1)
>> obj = Product.objects.get(id=1)
>> dir(obj) => see all different fields

In products/views.py:

from .models import Product

def product_detail_view(request):
	obj = Product.objects.get(id=1)
	context = {
		'object' : obj	
	}
	return render(request, "product/detail.html", {})
	
new folder in templates called product

inside this folder, create a file named detail.html

```
{% exends 'base.html' %}

{% block content %}
<h1>{{ object.title }}</h1>
<p> {{ object.description }} </p>
<p> {% if object.description %} {{ object.description }} {% else %} No description {% endif %}  </p>
{% endblock %}
```

Add entry to url.py

```
from products.views import product_detail_view

path('product/', product_detail_view)
```

**How Django Templates load with Apps**

**Django Model Forms**

Inside product make a new file called forms.py

```
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]
```

go into product/views.py:

```
from .forms import ProductForm

def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()	
		
	context = {
		'form' : form
	}
	
	return render(request, "products/product_create.html", context)

```

Create a new template product_create.html

```
{% extends 'base.html' %}

{% block content %}
<form method='POST'> {% csrf_token %}
{{ form.as_p }}
<input type='submit' value='Save' />
</form>
{% endblock %}
```

Add view to urls.py

```
from products.view import product_create_view

path('create', product_create_view),
```

**Raw html form**

2:13:38






















































