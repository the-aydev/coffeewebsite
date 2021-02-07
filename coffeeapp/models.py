from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    message = models.TextField()
