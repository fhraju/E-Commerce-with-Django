from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    name    = forms.CharField(label="Full Name",
                widget=forms.TextInput(
                        attrs={
                            "class": "form-control", 
                            "placeholder": "Your Full Name"
                        }
                    )
                )
    email   = forms.EmailField(required=False,
                widget=forms.EmailInput(
                        attrs={
                            "class": "form-control",
                            "placeholder": "Your Email"
                        }
                    )
                )
    content = forms.CharField(
                widget=forms.Textarea(
                        attrs={
                            "class": "form-control",
                            "placeholder": "Your Content Here"
                        }
                    )
                )
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Eamil need to be gmail.com")
        return email
