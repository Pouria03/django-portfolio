from django.db import models

class UserMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=11)
    body = models.TextField(max_length=500)

    def __str__(self):
        return self.name + ' ' + self.phone