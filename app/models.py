from django.db import models

# Create your models here.

class Contract(models.Model):
    contractname = models.CharField(max_length=50)
    md5 = models.CharField(max_length=100)
    sha1 = models.CharField(max_length=100)
    sha256 = models.CharField(max_length=100)
    filename =models.CharField(max_length=100)


class Member(models.Model):
    user_role = models.CharField(max_length=20)
    user_id = models.CharField(max_length=20, primary_key=True)
    user_name = models.CharField(max_length=20)
    user_pw = models.CharField(max_length=20)
    c_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.user_id