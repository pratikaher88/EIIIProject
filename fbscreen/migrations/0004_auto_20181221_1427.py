# Generated by Django 2.1.4 on 2018-12-21 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbscreen', '0003_feedbackinfoinputmodel_send_automated_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackinfoinputmodel',
            name='send_automated_data',
            field=models.BooleanField(default=False, verbose_name='I want to send automatically collected information'),
        ),
    ]