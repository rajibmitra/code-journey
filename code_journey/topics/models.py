from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')

class Problem(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='problems')
    name = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
