# Generated by Django 2.1.4 on 2018-12-21 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbscreen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackinfoinputmodel',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
    ]
