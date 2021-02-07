from django.urls import path

from . import views

app_name = 'coffeeapp'
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("numbers/", views.numbers, name="numbers"),
]
