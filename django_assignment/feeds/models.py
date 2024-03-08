from django.db import models

class User(models.Model):
    username= models.CharField(max_length=100,null=False)
    email = models.EmailField(max_length=100,verbose_name='Email',null=False)
    password = models.CharField(max_length=100,null=False)
    channel_subscription = models.BooleanField(default=False)

# class DistributedData(models.Model):
#     user = models.ForeignKey('User', related_name='User', on_delete=models.CASCADE)
#     channel_group = models.CharField(max_length=255)

