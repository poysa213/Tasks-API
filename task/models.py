from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description= models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return self.title
    class Meta:
        ordering  = ['complete']   
