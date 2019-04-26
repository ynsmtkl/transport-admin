from django.db import models


class Connect(models.Model):
    email = models.EmailField()
    secret = models.CharField(max_length=20)
