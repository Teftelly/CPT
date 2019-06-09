from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def publish(self):
        self.save()
        
    def __str__(self):
        return self.title
        
    def get_excerpt(self):
        return self.text[:140] + "..." if len(self.text) > 140 else self.text
        

# Create your models here.
