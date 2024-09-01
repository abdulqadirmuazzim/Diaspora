from django.urls import path
from . import views as v


urlpatterns = [
    path("", v.home, name="home"),
    path("contact", v.contact, name="contact"),
    path("zohoverify/verifyforzoho.html", v.zoho_verify, name="zoho"),
]
