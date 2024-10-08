from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from .form import ContactForm, SubForm
from .models import Contact, Subscription
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your views here.


# get the list of all staff
staff = User.objects.filter(is_staff=True)
staff_emails = [user.email for user in staff]


# home page
def home(req):
    if req.method == "POST":
        form = SubForm(req.POST)
        if form.is_valid():
            email = form.cleaned_data["SubEmail"]
            # send the user an email
            send_mail(
                "User Subscribed",
                f"Dear {email},\nThank you for subscribing to our news letter!",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            # send the staff an email
            send_mail(
                "Diasporia site",
                f"A user with email ({email}) has just subscribed to Diaspora news letter",
                settings.EMAIL_HOST_USER,
                staff_emails,
                fail_silently=False,
            )
            form.save()
            messages.success(req, "You have successfully subscribed!")
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
        # if form is valid
        if form.is_valid():
            # save the form
            form.save()
            # send an email to user
            send_mail(
                "Thanks for reaching out",
                f"Dear {name},\nThanks for reaching out to us.",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            # send an email to all staff
            send_mail(
                "Diasporia site",
                f"""
A user his just filled the contact form:\n
Name: {name},
Email: {email},
Phone: {phone},
Address: {address},
Message: {message},
                """,
                settings.EMAIL_HOST_USER,
                staff_emails,
                fail_silently=False,
            )

            messages.success(req, "Thanks for keeping in touch!")
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
def error_404(req, exception):
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
