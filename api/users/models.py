from django.db import models


class UserType(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


class Connect(models.Model):
    email = models.EmailField()
    secret = models.CharField(max_length=20)
    type = models.ForeignKey(UserType, on_delete=models.CASCADE)

    def __str__(self):
        return self.email


