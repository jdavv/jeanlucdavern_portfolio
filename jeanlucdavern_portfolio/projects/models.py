from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    repo = models.URLField()

    def __str__(self):
        return self.title

