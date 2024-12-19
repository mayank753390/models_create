from django.db import models

# Create your models here.
class Topic(models.Model):
    Topic_name=models.CharField(max_length=100,primary_key=True)

class Webpage(models.Model):
    Topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()

class AccessRecords(models.Model):
    Topic_name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()        