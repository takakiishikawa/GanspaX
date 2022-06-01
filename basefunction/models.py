from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)

    goal=models.CharField(max_length=100)
    coffee=models.BooleanField(max_length=100)
    job=models.CharField(max_length=100)
    fullname=models.CharField(max_length=100)
    coffee_like=models.CharField(max_length=100)

    class Meta:
        verbose_name='ユーザー情報'
        verbose_name_plural='ユーザー情報'

    def __str__(self):
        return self.fullname+'('+self.user.username+')'


class Ganspa_use(models.Model):
    ganspa_use=models.IntegerField()
    ganspa_use_datetime=models.DateTimeField()

    class Meta:
        verbose_name="入室回数"
        verbose_name_plural="入室回数"

    def __str__(self):
        return self.fullname+'('+self.user.username+')'
