from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from .form import ContactForm, SubForm
from django.contrib import messages

# Create your views here.


# home page
def home(req):
    if req.method == "POST":
        form = SubForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, "You have successfully subscribe")
            return redirect("home")
        else:
            messages.error(req, "An error accured")
            return redirect("home")
    return render(req, "Home.html")


# about page


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
def error_404(req, excption):
    return render(req, "404.html", status=404)


# 403 page
def error_403(req, exception):
    return render(req, "403.html", status=403)


# 400 page
def error_400(req, exception):
    return render(req, "400.html", status=400)


# 500 page
def error_500(req):
    return render(req, "500.html", status=500)


# Zoho verification
def zoho_verify(req):
    return render(req, "zohoverify/verifyforzoho.html")
