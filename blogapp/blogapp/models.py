from django.db import models
from django.contrib.auth.models import User
  
class Post(models.Model): 
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30, default='sameer')
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    comments = models.JSONField(default=list, blank=True)

    def __str__(self): 
        return self.title
    
class Comment(models.Model): 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='com')
    author = models.ForeignKey(User, on_delete=models.CASCADE )
    content = models.TextField()

    def __str__(self): 
        return self.author