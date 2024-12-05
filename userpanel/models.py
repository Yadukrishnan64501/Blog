from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings 

User=get_user_model()

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()
    product_image=models.ImageField(upload_to='products/')
    comment=models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='userpanel_blogs', default=3) 
    

    def __str__(self):
        return self.title

class ProfileUser(models.Model):
    
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=True)
    location=models.CharField(max_length=50,blank=True)
    profile_image = models.ImageField(upload_to='profile/')
    dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username  # Ensure this returns a string


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='userpanel_comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='userpanel_comments_user')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)  # Add this field

    def __str__(self):
        return f"{self.user.username}: {self.text[:20]}" 

class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp} - {self.user} - {self.action}"
    


