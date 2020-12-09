#Django
from django.db import models
from django.contrib.auth.models import User

#phone number field
from phonenumber_field.modelfields import PhoneNumberField


class School(models.Model):

    school = models.CharField(max_length=250, blank=True, null=True)
    principal_name = models.CharField(max_length=100, blank=True, null=True)
    principal_email = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.school)


class Coach(models.Model):

    coach_user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ManyToManyField(School)
    birthdate = models.DateField(blank=True, null=True)
    phone = PhoneNumberField()
    omegaup_user = models.CharField(max_length=150)

    def __str__(self):
        return str(self.user.username)


class Student(models.Model):

    student_user = models.OneToOneField(User, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True)
    school = models.ManyToManyField(School)
    birthdate = models.DateField(blank=True, null=True)
    name_of_tutor = models.CharField(max_length=150, blank=True, null=False)
    phone_of_tutor = PhoneNumberField()
    tutor_email = models.CharField(max_length=100, blank=True, null=True)
    omegaup_user = models.CharField(max_length=150)

    def __str__(self):
        return str(self.user.username)