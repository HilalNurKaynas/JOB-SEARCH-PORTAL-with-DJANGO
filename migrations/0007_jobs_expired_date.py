# Generated by Django 2.1.2 on 2018-11-23 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobPostingWebsite', '0006_jobapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='expired_date',
            field=models.DateField(null=True),
        ),
    ]