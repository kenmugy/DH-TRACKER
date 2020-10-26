from django.shortcuts import render
from .models import Contact


def home(request):
    contacts = Contact.object.all()
    return render(request, "track/home.html", {"contacts": contacts})


def contact(request):
    return render(request, "track/contact.html")

