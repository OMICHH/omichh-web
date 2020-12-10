from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):

    tag_name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return str(self.tag_name)


class Post(models.Model):

    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    post_title = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    content = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.post_title)


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return str(self.id)