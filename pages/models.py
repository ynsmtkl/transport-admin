from django.db import models
from django.forms import EmailField, CharField


class Connect(models.Model):
    email = EmailField()
    secret = CharField()
