from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title