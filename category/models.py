from django.db import models
from uuid import uuid4

from category.managers import CategoryManager

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    
    objects = CategoryManager()

    def __str__(self):
        return self.name