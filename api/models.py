from django.db import models
import string
import random

def gerarchave():
    
    length = 6
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

class Url(models.Model):
    id = models.AutoField(primary_key=True)
    url_original = models.URLField(max_length=500, null=False, blank=False)
    chave = models.CharField(max_length=10, null=True, blank=True, default=gerarchave, unique=True)
