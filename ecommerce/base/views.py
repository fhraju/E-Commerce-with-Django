from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ContactForm


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
