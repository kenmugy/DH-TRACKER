# from django.forms import modelform_factory,
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.messages import success
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm, UpdateContactForm
from django.views.generic import ListView 

from .filters import ContactFilter

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

    return render(request, "track/contact.html", {"form": form, title: 'Login'})

@login_required
def update_contact(request, id):
    contact_to_update = Contact.objects.get(pk=id)
    if request.method == "POST":
        form = UpdateContactForm(request.POST)
        if form.is_valid():
            new_temperature = form.cleaned_data.get("temperature")
            name = contact_to_update.name
            contact_to_update.temperature = new_temperature
            success(request, f"{name}'s new temperature is {new_temperature}")
            contact_to_update.save()
            return redirect("home")
    else:
        form = UpdateContactForm(initial={'temperature': contact_to_update.temperature, title: 'Update'})
    return render(
        request,
        "track/update_contact.html",
        {"form": form, "contact": contact_to_update},
    )

@login_required
def contact_search(request):
    context = {'title': 'Home'}
    contact_filter = ContactFilter(request.GET, queryset=Contact.objects.all().order_by('-date'))
    context['filtered_contacts'] = contact_filter
    return render(request, 'track/contact_search.html', context=context)

def landing_page(request):
    return render(request, 'track/landing_page.html', context={'title', 'Landing'})







# ContactForm = modelform_factory(Contact, exclude=[])



# @login_required
# def home(request):
#     contacts = get_list_or_404(Contact) 
#     return render(request, "track/home.html", {"contacts": contacts})

# class ContactListView(ListView):
#     model = Contact
#     template_name = 'track/home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter'] = ContactFilter(self.request.GET, queryset = self.get_queryset())
#         return context