from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    #creating relationship with User model
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #extending attributes with additionals
    portfolio = models.URLField(blank=True)
    profile_pictures = models.ImageField(upload_to='profile_pictures',blank=True)

    def __str__(self):
        return self.user.username
