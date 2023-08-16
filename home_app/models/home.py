from django.db import models
from home_app.models import BaseModel

class Home(BaseModel):
    image = models.ImageField(upload_to='images/home/')

    def __str__(self):
        return self.full_name + ' ' + self.job_title
