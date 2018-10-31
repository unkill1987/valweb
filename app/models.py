from django.db import models

# Create your models here.

class Contract(models.Model):
    contractname = models.CharField(max_length=50)
    md5 = models.CharField(max_length=100)
    sha1 = models.CharField(max_length=100)
    sha256 = models.CharField(max_length=100)
    filename =models.CharField(max_length=100)
