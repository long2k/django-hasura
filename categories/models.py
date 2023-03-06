from django.db import models

class Category(models.Model):
    name = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank= True)
    updated = models.DateTimeField(null=True)