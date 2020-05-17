from django.db import models
# from django.conf import settings
from  django.contrib.auth.models import User
# from django
# Create your models here.
class userProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    protofolio_site = models.URLField(blank= True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
