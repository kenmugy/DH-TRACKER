from django.urls import path
from .views import contact_search, contact, update_contact

urlpatterns = [
    path("", contact_search, name="home"),
    path("contact/", contact, name="contact"),
    path("update/<int:id>", update_contact, name="update"),
]

