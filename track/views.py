from django.shortcuts import render, redirect, get_list_or_404
from django.forms import modelform_factory
from django.contrib.messages import success
from django.contrib.auth.decorators import login_required

from .models import Contact
from .forms import ContactForm, UpdateContactForm

# ContactForm = modelform_factory(Contact, exclude=[])


@login_required
def home(request):
    contacts = get_list_or_404(Contact)
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


def update_contact(request):
    form = UpdateContactForm()

    # if request.method == 'POST':
    #     form = UpdateContactForm(instance=)
    return render(request, "track/update_contact.html", {"form": form})

