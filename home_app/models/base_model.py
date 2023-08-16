from django.db import models

class BaseModel(models.Model):
    full_name = models.CharField(max_length=250)
    job_title = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    class Meta:
        abstract=True