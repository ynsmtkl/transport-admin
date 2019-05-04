from django.db import models

from api.users.models import UserConnect


class Parent(models.Model):
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    user_connect = models.ForeignKey(UserConnect, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_connect.email


class Student(models.Model):
    cne = models.CharField(max_length=20)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return self.parent.user_connect.email


class Driver(models.Model):
    license = models.CharField(max_length=10)
    date_licence = models.DateField()
    user_connect = models.ForeignKey(UserConnect, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_connect.email


class Bus(models.Model):
    nb_place = models.IntegerField()
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
    student = models.ManyToManyField(Parent)
