# Generated by Django 4.2.4 on 2023-08-17 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0002_remove_generalsiteinfo_site_icon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalsiteinfo',
            name='fav_icon',
            field=models.ImageField(blank=True, null=True, upload_to='images/favicon/'),
        ),
    ]
