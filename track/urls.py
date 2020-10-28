from django.urls import path
from .views import home, contact, update_contact

urlpatterns = [
    path("", home, name="home"),
    path("contact/", contact, name="contact"),
    path("update/<int:id>", update_contact, name="update"),
]

