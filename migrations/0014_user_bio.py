# Generated by Django 2.1.2 on 2018-11-25 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobPostingWebsite', '0013_auto_20181124_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(max_length=2500, null=True),
        ),
    ]