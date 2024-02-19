from django.db import models
from django.db.models import Model


class Category(models.Model):
    
    name = models.CharField(max_length=255, name="name", null ="True")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, name= "title" , null=True)
    blog_banner = models.ImageField(upload_to='blog_banners/')
    content = models.TextField()
    category =models.ForeignKey("Category", on_delete=models.CASCADE)
    author_name =models.ForeignKey("Author", on_delete=models.CASCADE , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (('draft', 'Save Draft'), ('published', 'Published'))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
    
    
class Author(models.Model):
    author_name = models.CharField(max_length=100, name ="author_name")
    
    def __str__(self):
     return self.author_name 
 
class Comment(models.Model):
    post =models.ForeignKey("Post", on_delete =models.CASCADE, null=True)
    name =models.CharField(max_length =100)
    email =models.CharField(max_length =200)
    message =models.TextField()
    
    def __str__(self):
        return self.name  
    


# Create your models here.
