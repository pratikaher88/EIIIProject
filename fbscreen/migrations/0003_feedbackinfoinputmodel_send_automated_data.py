# Generated by Django 2.1.4 on 2018-12-21 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbscreen', '0002_feedbackinfoinputmodel_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackinfoinputmodel',
            name='send_automated_data',
            field=models.BooleanField(default=False),
        ),
    ]