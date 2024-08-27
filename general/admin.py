from django.contrib import admin
from .models import Contact, Subscription


class displayContact(admin.ModelAdmin):
    list_display = ["Name", "Email" "Phone"]


# Register your models here.
admin.site.register(Contact)
admin.site.register(Subscription)
