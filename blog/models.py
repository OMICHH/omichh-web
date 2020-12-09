from django.db import models


class Tag(models.Model):

    tag_name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return str(self.tag_name)
