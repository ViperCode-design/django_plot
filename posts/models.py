from django.db import models
from accounts.models import  owner

# Create your models here.

class post(models.Model):
    owner = models.ForeignKey(owner, on_delete=models.CASCADE, related_name='post_owner' )
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    date_created = models.DateTimeField(auto_now_add=True)
    number_of_likes = models.IntegerField(default=0)
    number_of_comments = models.IntegerField(default=0)


    def __str__(self):
        return self.description



class comment(models.Model):
    owner = models.ForeignKey(owner, on_delete=models.CASCADE, related_name='comment_owner')
    post = models.ForeignKey(post, on_delete=models.CASCADE, related_name='comment_post')
    content = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.user_name