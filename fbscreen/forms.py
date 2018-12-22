from django import forms
from django.shortcuts import render, redirect
from dal import autocomplete

from .models import FeedbackInfoInputModel

class FeedbackInfoInputModelForm(forms.ModelForm):

	request_accessible_version = forms.BooleanField(label='I want to request an accessible version of content ',required=False)


	class Meta:
		model = FeedbackInfoInputModel
		fields = ['site_name','content','description','send_automated_data']
		widgets = { 'content' : autocomplete.ListSelect2(url='content-autocomplete') }
		# ,forward=['site_name']
		queryset = {'content' : FeedbackInfoInputModel.objects.all() }

	def __init__(self, *args, **kwargs):
		super(FeedbackInfoInputModelForm, self).__init__(*args, **kwargs)
		self.fields['content'].widget = forms.TextInput(attrs={
			'id': 'contentfieldid',
			})

		self.fields['request_accessible_version'].widget = forms.CheckboxInput(attrs={
			'id': 'requestcheckbox',
			})

	field_order = ['site_name','description', 'request_accessible_version' ,'content' ,'send_automated_data','captcha']