from django.db import models

# Create your models here.

class owner(models.Model):
    user_name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15)
    bio = models.TextField(null=True)
    profile_picture = models.ImageField(default='accounts/user.png')
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user_name


