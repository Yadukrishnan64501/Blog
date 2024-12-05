from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    profile_description=models.TextField(20)
    phone=models.CharField(max_length=15,unique=True)
    profile_image=models.ImageField(upload_to='profile_images/')
    id_proof=models.ImageField(upload_to='profile_images/')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)  # Added field

    def __str__(self):
        return self.user.username
        


class blog(models.Model):
    STATUS_CHOICES =(
        ('publish','Publish'),
        ('draft','Draft'),
        ('hidden','Hidden',)
    )
    title=models.CharField(max_length=50)
    content=models.TextField(50)
    blog_image=models.ImageField(upload_to='blog_images/')
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    is_visible = models.BooleanField(default=True)  # Added field

    def __str__(self):
        return self.title


class comment(models.Model):
    STATUS_CHOICES =(
        ('show','Show'),
        ('hidden','Hidden',)
    )
    comment=models.TextField(20)
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='adminpanel_comments_user')
    blog=models.ForeignKey(blog, on_delete=models.CASCADE,related_name='adminpanel_comments')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='show')
    is_visible = models.BooleanField(default=True)  # Added field


    def __str__(self):
        return self.comment


    

    
