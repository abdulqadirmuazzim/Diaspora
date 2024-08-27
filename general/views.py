from django.shortcuts import render

# Create your views here.


# home page
def home(req):
    return render(req, "Home.html")


# about page
def about(req):
    return render(req, "about2.html")


# contact page
def contact(req):
    return render(req, "contact.html")
