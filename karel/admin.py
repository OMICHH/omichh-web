from django.contrib import admin
from karel.models import  Problem, KarelVideo


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):

    list_display = ('problem_name',)
    list_display_links = ('problem_name',)
    search_fields = ('problem_name',)


@admin.register(KarelVideo)
class KarelAdmin(admin.ModelAdmin):

    list_display = ('order', 'title', 'video_url')
    list_display_links = ('order', 'title')
    list_editable = ('video_url',)
    search_fields = ('title',)