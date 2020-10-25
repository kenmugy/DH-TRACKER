from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm


def login(request):
    form = AuthenticationForm()
    return render(request, "users/login", {"form": form})

