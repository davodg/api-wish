from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.


class Wish(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, default=User)
    id_wish = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    link = models.CharField(max_length=255, blank=True)
    image = models.URLField(max_length=255, null=True, blank=True)
    acquired = models.BooleanField(default=False, null=True)
    

    def __str__(self):
        return self.title
