from django import forms
from .models import Contact, Subscription


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["Name", "Email", "Phone", "Address", "Message"]

    # we can add custom validation for "Phone"
    # def clean_phone(self):
    #     if self.is_valid():
    #         phone = self.cleaned_data['Phone']
    #         if not ''.startswith("+"):
    #             return self.add_error('Phone', "Should be like this '+234...'")


class SubForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ["SubEmail"]
