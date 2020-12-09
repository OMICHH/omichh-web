from django.db import models
from blog.models import Tag


class Problem(models.Model):
    problem_name = models.CharField(max_length=150)
    url = models.URLField(max_length=255)

    def __str__(self):
        return str(self.problem_name)


class Karel(models.Model):

    title = models.CharField(max_length=150)
    tag = models.ManyToManyField(Tag)
    problem_set = models.ManyToManyField(Problem)
    order = models.IntegerField()
    video_url = models.URLField(max_length=255)

    def __str__(self):
        return str(self.title)

