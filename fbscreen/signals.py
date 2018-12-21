from .models import FeedbackInfoInputModel
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage

from fbscreen.models import FeedbackInfoInputModel

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



# @receiver(post_save,sender=FeedbackInfoInputModel)
# def send_email(sender,instance,created,**kwargs):
#     logging.info('Hello')

# 	if instance.status=='Resolved':


# 		logging.info('Hello')

		# email = EmailMessage('title', 'body', to='pratikaher88@gmail.com')
		# email.send()
