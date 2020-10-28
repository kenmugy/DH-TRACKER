from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.forms import modelform_factory
from django.contrib.messages import success
from django.contrib.auth.decorators import login_required

from .models import Contact
from .forms import ContactForm, UpdateContactForm

# ContactForm = modelform_factory(Contact, exclude=[])


@login_required
def home(request):
    contacts = get_list_or_404(Contact) or None
    return render(request, "track/home.html", {"contacts": contacts})


@login_required
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            success(request, f"{name} successfully added")
            form.save()
            return redirect("home")
    else:
        form = ContactForm()

    return render(request, "track/contact.html", {"form": form})


def update_contact(request, id):
    contact_to_update = Contact.objects.get(pk=id)
    if request.method == "POST":
        form = UpdateContactForm(request.POST)
        if form.is_valid():
            new_temperature = form.cleaned_data.get("temperature")
            contact_to_update.temperature = new_temperature
            contact_to_update.save()
            return redirect("home")
    else:
        form = UpdateContactForm()
    return render(
        request,
        "track/update_contact.html",
        {"form": form, "contact": contact_to_update},
    )

