#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth.models import User
from users.models import Coach, Student, School, Category


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('coach_user', 'coach_email','omegaup_user')
    list_display_links = ('coach_user','coach_email','omegaup_user')
    search_fields = ('coach_user','coach_email','omegaup_user')
    list_filter =  ('coach_user__is_active',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = ('student_user', 'coach', 'school', 'omegaup_user')
    list_display_links = ('student_user',)
    search_fields = ('student_user', 'omegaup_user')
    list_filter =  ('student_user__is_active',)


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school','principal_name','principal_email')
    list_display_links = ('school','principal_name','principal_email')
    search_fields = ('school','principal_name','principal_email')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','school_level')
    list_display_links = ('category_name','school_level')
    search_fields = ('category_name','school_level')