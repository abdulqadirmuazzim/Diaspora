from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from .form import ContactForm, SubForm

# Create your views here.


# home page
def home(req):
    return render(req, "Home.html")


# about page
def about(req):
    return render(req, "about2.html")


# contact page
def contact(req):
    if req.method == "POST":
        form = ContactForm(req.POST)
        name = req.POST["Name"]
        email = req.POST["Email"]
        phone = req.POST["Phone"]
        address = req.POST["Address"]
        message = req.POST["Message"]
        print(form)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            errors = form.errors.values()
            return render(
                req,
                "contact.html",
                {
                    "errors": errors,
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "address": address,
                    "message": message,
                },
            )
    return render(req, "contact.html")


# 404 page
def error(req, execrption):
    return page_not_found(req, template_name="404.html")
