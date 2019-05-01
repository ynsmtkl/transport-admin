from django.db import models


class UserType(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


class UserConnect(models.Model):
    email = models.EmailField()
    secret = models.CharField(max_length=20)
    userType = models.ForeignKey(UserType, on_delete=models.CASCADE)
    date_star = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return self.email


