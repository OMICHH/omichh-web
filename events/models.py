from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()

    type_choices = [
        ('Test', 'Test'),
        ('Important','Important'),
        ('Meeting','Meeting')
    ]

    type_event = models.CharField(max_length=100, choices=type_choices, null=False)

    def __str__(self):
        return str(self.title)
