import django_filters
from .models import Contact


class ContactFilter(django_filters.FilterSet):
    class Meta:
        model = Contact
        fields = ["name", "telephone"]

