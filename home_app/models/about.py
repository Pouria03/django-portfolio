from django.db import models
from home_app.models import BaseModel

# Create your models here.
class About(BaseModel):
    years_of_experience = models.IntegerField(default=0)
    projects_quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/about/')

    def __str__(self) -> str:
        return self.full_name + ' - ' + self.job_title