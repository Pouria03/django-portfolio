from django.contrib import admin
from home_app import models


# Register your models here.
admin.site.register(models.About)
admin.site.register(models.GeneralSiteInfo)
admin.site.register(models.Home)
admin.site.register(models.Resume)
admin.site.register(models.Service)
admin.site.register(models.Skill)
admin.site.register(models.UserMessage)