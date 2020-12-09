#Django
from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ManyToManyField(School, verbose_name=_("Schools"))
    birthdate = models.DateField(blank=True, null=True)
    phone = models.PhoneNumberField()
    omegaup_user = models.CharField(max_length=150)

    def __str__(self):
        return str(self.user.username)


class Student(models.Model):

    user = models.OneToOneField(User, verbose_name=_("Students"), on_delete=models.CASCADE)
    coach = models.OneToOneField(Coach, verbose_name=_("Coaches"), on_delete=models.SET_NULL)
    school = models.ManyToManyField(School, verbose_name=_("Schools"))
    birthdate = models.DateField(blank=True, null=True)
    name_of_tutor = models.CharField(max_length=150, ${blank=True, null=False})
    phone_of_tutor = models.PhoneNumberField()
    tutor_email = name = models.CharField(max_length=100, ${blank=True, null=True})
    omegaup_user = models.CharField(max_length=150)


class School(models.Model):

    name = models.CharField(max_length=250, ${blank=True, null=True})
    principal_name = name = models.CharField(max_length=100, ${blank=True, null=True})
    principal_email = name = models.CharField(max_length=100, ${blank=True, null=True})

    def __str__(self):
        return str(self.name)
