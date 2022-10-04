
from django.db import models

# Create your models here.

class Like(models.Model):
    like_count = models.CharField(max_length=64)
