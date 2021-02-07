from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactUsForm


def index(response):
    return render(response, 'coffeeapp/index.html', {})


def about(response):
    return render(response, 'coffeeapp/about.html', {})


def contact(response):
    if response.method == "POST":
        form = ContactUsForm(response.POST)
        if form.is_valid():
            HttpResponseRedirect('/thanks')
    else:
        form = ContactUsForm()
    return render(response, 'coffeeapp/contact.html', {"form": form})


def numbers(response):
    return render(response, 'coffeeapp/numbers.html', {})
