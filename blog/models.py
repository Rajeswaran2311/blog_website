from django.db import models

# Create your models here.
class ai(models.Model):
    headline = models.CharField(max_length=300)
    img = models.URLField(null=True, blank=True)
    url = models.TextField()
    def __str__(self):
        return self.headline
class user(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)
    
