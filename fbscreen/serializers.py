from rest_framework import serializers
from .models import FeedbackInfoInputModel

class FeedbackInfoInputModelSerializer(serializers.ModelSerializer):

	class Meta:
		model = FeedbackInfoInputModel
		fields = ['description','content']