from django.db import models

class QueryLog(models.Model):
    query = models.TextField()
    tone = models.CharField(max_length=1000)
    intent = models.CharField(max_length=1000)
    suggested_actions = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)
