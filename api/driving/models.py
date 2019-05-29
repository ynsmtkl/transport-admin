from django.contrib.auth.models import User
from django.db import models


class Parent(models.Model):
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Student(models.Model):
    cne = models.CharField(max_length=20)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Driver(models.Model):
    license = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Bus(models.Model):
    nb_place = models.IntegerField()
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
    student = models.ManyToManyField(Parent)

    def __str__(self):
        return "Bus: " + str(self.id)
