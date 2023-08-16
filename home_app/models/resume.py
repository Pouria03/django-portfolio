from django.db import models

class Resume(models.Model):
    image = models.ImageField(upload_to='images/resume')
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500,blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title + ' ' + self.level