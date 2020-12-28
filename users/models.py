#Django
from django.db import models
from django.contrib.auth.models import User

#phone number field
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):

    category_name = models.CharField(max_length=10, blank=False, null=False)
    school_level = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.school_level)

    def Meta(self):
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class School(models.Model):

    school = models.CharField(max_length=250, blank=True, null=True)
    principal_name = models.CharField(max_length=100, blank=True, null=True)
    principal_email = models.EmailField(max_length=254)

    def __str__(self):
        return str(self.school)


class Coach(models.Model):

    coach_user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ManyToManyField(School)
    birthdate = models.DateField(blank=True, null=True)
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    omegaup_user = models.CharField(max_length=150)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return str(self.coach_user.username)

    def Meta(self):
        verbose_name = _('Coach')
        verbose_name_plural = _('Coaches')


class Student(models.Model):

    student_user = models.OneToOneField(User, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True)
    school = models.ForeignKey(School,on_delete=models.SET_NULL, null=True)
    birthdate = models.DateField(blank=True, null=True)
    name_of_tutor = models.CharField(max_length=150, blank=True, null=False)
    phone_of_tutor = PhoneNumberField(null=True, blank=False, unique=True)
    tutor_email = models.EmailField(max_length=254)
    omegaup_user = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.student_user.username)
