from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1> Hello World </h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about me",
        "my_number": 123,
        "my_list": [123, 345]
    }
    return render(request, "contact.html", my_context)