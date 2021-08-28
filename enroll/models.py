from django.db import models

# Create your models here.
class Post(models.Model):
  image = models.ImageField()
  title = models.CharField(max_length=255)
  description = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['-date']
  
  def __str__(self):
    return self.title