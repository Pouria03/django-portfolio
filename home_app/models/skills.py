from django.db import models

class Skill(models.Model):
    title = models.CharField(max_length=150)
    level = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.title + ' ' + self.level