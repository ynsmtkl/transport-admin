from django.db import models


class Connect(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    date = models.DateField()

    def __str__(self):
        return self.username
