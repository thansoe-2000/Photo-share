from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Photo(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    