from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.driving.models import Parent, Driver, Student


class EditUserSerializer(serializers.ModelSerializer):

    username = serializers.CharField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]

    def update(self, instance, validated_data):
        instance.first_name = validated_data["first_name"]
        instance.last_name = validated_data["last_name"]

        instance.save()

        return validated_data


class EditParentSerializer(serializers.ModelSerializer):
    user = EditUserSerializer()

    class Meta:
        model = Parent
        fields = [
            'phone',
            'city',
            'address',
            'user',
        ]

    def validate(self, data):
        user_data = data.pop("user")

        user = User.objects.filter(username=user_data.get("username"))

        if not user.exists():
            raise ValidationError("This user doesn't exist!")

        data["user"] = user.first()
        data["first_name"] = user_data.get("first_name")
        data["last_name"] = user_data.get("last_name")

        return data

    def create(self, validated_data):
        user = validated_data["user"]
        phone = validated_data["phone"]
        city = validated_data["city"]
        address = validated_data["address"]

        email = user.email
        parent_obj = None

        parent = Parent.objects.filter(user__email=email)
        if parent.exists():
            parent_obj = parent.first()
            parent_obj.phone = phone
            parent_obj.city = city
            parent_obj.address = address
            parent_obj.user = user
        else:
            parent_obj = Parent(phone=phone,city=city,address=address,user=user)

        user_obj = User.objects.filter(email=email)
        user_instance = user_obj.first()

        user_instance.first_name = validated_data["first_name"]
        user_instance.last_name = validated_data["last_name"]
        user_instance.save()

        parent_obj.save()

        return validated_data


class EditDriverSerializer(serializers.ModelSerializer):
    user = EditUserSerializer()

    class Meta:
        model = Driver
        fields = [
            'license',
            'user',
        ]

    def validate(self, data):
        user_data = data.pop("user")

        user = User.objects.filter(username=user_data.get("username"))

        if not user.exists():
            raise ValidationError("This user doesn't exist!")

        data["user"] = user.first()
        data["first_name"] = user_data.get("first_name")
        data["last_name"] = user_data.get("last_name")

        return data

    def create(self, validated_data):
        user = validated_data["user"]
        license = validated_data["license"]

        email = user.email
        driver_obj = None

        driver = Driver.objects.filter(user__email=email)
        if driver.exists():
            driver_obj = driver.first()
            driver_obj.license = license
            driver_obj.user = user
        else:
            driver_obj = Driver(license=license, user=user)

        driver_obj.save()

        user_obj = User.objects.filter(email=email)
        user_instance = user_obj.first()

        user_instance.first_name = validated_data["first_name"]
        user_instance.last_name = validated_data["last_name"]
        user_instance.save()

        return validated_data


class EditStudentSerializer(serializers.ModelSerializer):
    user = EditUserSerializer()
    email_parent =  serializers.EmailField()

    class Meta:
        model = Student
        fields = [
            'cne',
            'email_parent',
            'user',
        ]

    def validate(self, data):
        user_data = data.pop("user")
        email_parent = data.get("email_parent")

        user = User.objects.filter(username=user_data.get("username"))

        if not user.exists():
            raise ValidationError("This user doesn't exist!")

        parent = Parent.objects.filter(user__email=email_parent)
        if not parent.exists():
            raise ValidationError("This parent doesn't exist!")

        if email_parent == user_data.get("email"):
            raise ValidationError("Your email and your parent's email should be different!")

        data["parent"] = parent.first()
        data["user"] = user.first()
        data["first_name"] = user_data.get("first_name")
        data["last_name"] = user_data.get("last_name")

        return data

    def create(self, validated_data):
        parent = validated_data["parent"]
        user = validated_data["user"]
        cne = validated_data["cne"]

        email = user.email
        student_obj = None

        student = Student.objects.filter(user__email=email)
        if student.exists():
            student_obj = student.first()
            student_obj.cne = cne
            student_obj.parent = parent
            student_obj.user = user
        else:
            student_obj = Student(cne=cne, parent=parent, user=user)

        student_obj.save()

        user_obj = User.objects.filter(email=email)
        user_instance = user_obj.first()

        user_instance.first_name = validated_data["first_name"]
        user_instance.last_name = validated_data["last_name"]
        user_instance.save()

        return validated_data
