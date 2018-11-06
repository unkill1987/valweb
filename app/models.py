from django.db import models


# Create your models here.


class Member(models.Model):
    user_role = models.CharField(max_length=20)
    user_id = models.CharField(max_length=20, primary_key=True)
    user_name = models.CharField(max_length=20)
    user_pw = models.CharField(max_length=20)
    c_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.user_id


class Contract(models.Model):
    contractname = models.CharField(max_length=50)
    sha256 = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    share1 = models.CharField(max_length=100)
    share2 = models.CharField(max_length=100)
    share3 = models.CharField(max_length=100)
    share4 = models.CharField(max_length=100)

class Contract_LC(models.Model):
    contractname = models.CharField(max_length=50)
    sha256 = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    share1 = models.CharField(max_length=100)
    share2 = models.CharField(max_length=100)
    share3 = models.CharField(max_length=100)
    share4 = models.CharField(max_length=100)


class Contract_CI(models.Model):
    contractname = models.CharField(max_length=50)
    sha256 = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    share1 = models.CharField(max_length=100)
    share2 = models.CharField(max_length=100)
    share3 = models.CharField(max_length=100)
    share4 = models.CharField(max_length=100)


class Contract_SR(models.Model):
    contractname = models.CharField(max_length=50)
    sha256 = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    share1 = models.CharField(max_length=100)
    share2 = models.CharField(max_length=100)
    share3 = models.CharField(max_length=100)
    share4 = models.CharField(max_length=100)


class Contract_BL(models.Model):
    contractname = models.CharField(max_length=50)
    sha256 = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    share1 = models.CharField(max_length=100)
    share2 = models.CharField(max_length=100)
    share3 = models.CharField(max_length=100)
    share4 = models.CharField(max_length=100)


class Contract_DO(models.Model):
    contractname = models.CharField(max_length=50)
    sha256 = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    share1 = models.CharField(max_length=100)
    share2 = models.CharField(max_length=100)
    share3 = models.CharField(max_length=100)
    share4 = models.CharField(max_length=100)