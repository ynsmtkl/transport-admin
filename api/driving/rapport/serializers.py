from collections import OrderedDict

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.driving.models import Student, Parent


# Create your dictionary class
class MyDic(dict):

    # __init__ function
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value


class UserSerialize(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
        ]

        extra_kwargs = {
            'first_name' : {
                'read_only' : True
            },
            'last_name' : {
                'read_only' : True
            }
        }


class ParentSerializer(serializers.ModelSerializer):
    user = UserSerialize()

    class Meta:
        model = Parent
        fields = [
            'user'
        ]


class GetStudentsSerializer(serializers.Serializer):
    parent = ParentSerializer()

    class Meta:
        model = Student
        fields = [
            'parent',
        ]

    def validate(self, data):
        parent = data.get("parent")
        user = parent.get("user")
        email = user.get("email")

        student_set = Student.objects.filter(parent__user__email=email)
        if not student_set.exists():
            raise ValidationError("This parent doesn't exist!")

        i = 1
        myData = {}
        myData["student"] = []


        for student in student_set:
            myStudent = MyDic()
            myStudent.add('first_name',student.user.first_name)
            myStudent.add('last_name',student.user.last_name)
            myData["student"].append(myStudent)

        # myUser["user"] = my_dic
        # myData["parent"] = myUser
        print(myData)

        return myData

