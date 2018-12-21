from django.db import models
from django.core.validators import URLValidator
import random
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import EmailMessage


import logging, logging.config
import sys

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}

logging.config.dictConfig(LOGGING)

class FeedbackInfoInputModel(models.Model):

	def random_string():
		return str(random.randint(10000, 99999))

	site_name = models.CharField(max_length=100,validators=[URLValidator()])
	Number = models.CharField(max_length=100 ,blank=True, unique=True, default=random_string)
	description = models.TextField(max_length=500, verbose_name='Please describe accessibility problem')
	content = models.CharField(max_length=100,blank=True , verbose_name='Please describe the content you need. For example, document name, or name of a video file.')
	created_at = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=100, default="Open")
	email = models.EmailField(max_length=100 ,blank=True)
	send_automated_data = models.BooleanField(default=False, verbose_name='I want to send automatically collected information')



@receiver(post_save,sender=FeedbackInfoInputModel)
def send_email(sender,instance,created,**kwargs):


	if instance.status=='Resolved':

		email = EmailMessage('Ticket Status for '+instance.Number, 'Your issue is '+instance.status, to=['pratikaher88@gmail.com'])
		email.send()

		logging.info(instance.status)



# class UserForEmail(models.Model):

# 	email = models.EmailField(max_length=70)
# 	datafromfeedback = models.Foreignkey(FeedbackInfoInputModel,on_delete='CASACDE')	
