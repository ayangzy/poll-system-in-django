from django.db import models

# Create your models here.


class Contestant(models.Model):
    name = models.CharField(max_length=200)
    school = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    votes_total = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)


def __str__(self):
    return self.name
