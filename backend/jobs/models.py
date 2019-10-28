from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.text import slugify
import itertools

class Job(models.Model):
    title = models.CharField(max_length=140, blank=False)
    location = models.CharField(max_length=140, blank=False)
    company = models.CharField(max_length=140, blank=False)
    applicationLink = models.CharField(max_length=1000, blank=False)
    languages = ArrayField(models.CharField(max_length=140, blank=True), size=26) # size = total number of languages
    description = models.TextField(max_length=1000, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Return a human readable representation of the model instance. """
        return "{}".format(self.title)