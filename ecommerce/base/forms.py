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
    

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    username = forms.CharField()
    email    = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username already taken give another")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already exist")
        return email

    def clean(self):
        data = self.cleaned_data
        if data["password"] != data["password2"]:
            raise forms.ValidationError("Password must be same")
        return data

