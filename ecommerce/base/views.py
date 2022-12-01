from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        "title": "This is the Home Page",
        "content": "This is a Content",
    }
    if request.user.is_authenticated:
        context["premium_content"] = "Hell YEAAAAAAAAAA"
    return render(request, "base/home_page.html", context)

def about_page(request):
    context = {
        "title": "This is the About Page"
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    form = ContactForm(request.POST or None)
    context = {
        "title": "This is the Contact Page",
        "form": form,
        "brand": "New Brand Name"
    }
    
    return render(request, "contact/view.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("User logged in ")
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
        else:
            print("Login Error")

    return render(request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, "auth/register.html", context)
