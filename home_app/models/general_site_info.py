from django.db import models

class GeneralSiteInfo(models.Model):
    fav_icon = models.ImageField(upload_to='images/favicon/',blank=True,null=True)
    site_name = models.CharField(max_length=100)
    instagram = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)
    whatsapp = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=11)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(max_length=500)

    def __str__(self):
        return self.phone + ' ' + self.email