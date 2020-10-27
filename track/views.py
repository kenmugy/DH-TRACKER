from django.shortcuts import render, get_list_or_404
from django.forms import modelform_factory
from .models import Contact

ContactForm = modelform_factory(Contact, exclude=[])


def home(request):
    contacts = get_list_or_404(Contact)
    return render(request, "track/home.html", {"contacts": contacts})


def contact(request):
    return render(request, "track/contact.html")


def new(request):
    form = ContactForm()
    return render(request, "track/new.html", {"form": form})

