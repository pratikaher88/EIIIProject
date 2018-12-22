import json
import urllib
from django.http import Http404
from rest_framework import generics
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect,get_object_or_404
from .forms import FeedbackInfoInputModelForm
from .models import FeedbackInfoInputModel
from .serializers import FeedbackInfoInputModelSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView,DetailView,CreateView,UpdateView,UpdateView,DeleteView
from dal import autocomplete


def home(request):

	if request.method == 'POST':
		form = FeedbackInfoInputModelForm(request.POST)

		if form.is_valid():
			recaptcha_response = request.POST.get('g-recaptcha-response')
			url = 'https://www.google.com/recaptcha/api/siteverify'
			values = {
			'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
			'response': recaptcha_response
			}
			data = urllib.parse.urlencode(values).encode()
			req =  urllib.request.Request(url, data=data)
			response = urllib.request.urlopen(req)
			result = json.loads(response.read().decode())


			if result['success']:

				form.save()
				request.session['home_request'] = True
				return redirect('email-fetch')

			else:
				messages.warning(request, 'Invalid reCAPTCHA. Please try again.')
				return render(request, 'form_template.html', {'form': form})

	else:

		form = FeedbackInfoInputModelForm()

	return render(request, 'form_template.html', {'form': form})

def emailfetch(request):

	if 'home_request' in request.session:

		latest_field = FeedbackInfoInputModel.objects.last()

		if request.method == 'POST':

			if request.POST.get('submit')=='submit':

				email = request.POST.get('email')

				if email == None:
					return redirect('email-fetch')

				latest_field.email=email
				latest_field.save()

				messages.success(request , 'Email Added')

				del request.session['home_request']

				return redirect('list-entries')

			elif request.POST.get('cancel')=='cancel':

				del request.session['home_request']
				messages.warning(request , 'Email Not Added')
				return redirect('list-entries')

		

		return render(request,'email_fetch.html',{'latest_field':latest_field})


	raise Http404

def findstatusofid(request):

	if request.method == 'POST':
		id = request.POST.get('search_id')

		try:
			value = get_object_or_404(FeedbackInfoInputModel,Number=id)

			return render(request,'details_page.html',{'details':value })

		except:
			messages.warning(request , 'Invalid ID')
			return redirect('findstatus')

	return render(request,'find_status.html',{'id':1})

def detailspage(request, pk):

	details = get_object_or_404(FeedbackInfoInputModel,pk=pk)
	return render(request,'details_page.html',{'details' : details ,'object_no': pk} )

def list_entries(request):

	feedbackvalues = FeedbackInfoInputModel.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(feedbackvalues, 5)

	try:
		feedbackvalues = paginator.page(page)
	except PageNotAnInteger:
		feedbackvalues = paginator.page(1)
	except EmptyPage:
		feedbackvalues = paginator.page(paginator.num_pages)

	return render(request,'list_entries.html', {'feedbackvalues': feedbackvalues})

def list_entries_for_site(request):

	feedbackvalues = FeedbackInfoInputModel.objects.filter(site_name=request.GET['site_name'])
	feedbackvaluescount = feedbackvalues.count()

	page = request.GET.get('page', 1)
	paginator = Paginator(feedbackvalues, 5)

	try:
		feedbackvalues = paginator.page(page)
	except PageNotAnInteger:
		feedbackvalues = paginator.page(1)
	except EmptyPage:
		feedbackvalues = paginator.page(paginator.num_pages)

	return render(request,'list_entries.html', {'feedbackvalues': feedbackvalues,'feedbackvaluescount': feedbackvaluescount})

class ContentAutoComplete(autocomplete.Select2QuerySetView):

	def get_queryset(self):

		qs = FeedbackInfoInputModel.objects.all()

		site_name = self.forwarded.get('site_name', None)

		# if site_name:
		# 	qs = qs.filter(site_name=site_name)

		if self.q:
			qs = qs.filter(content__istartswith = self.q)
			return qs

class ListFeedbackInfoInputModelView(generics.ListAPIView):
    queryset = FeedbackInfoInputModel.objects.all()
    serializer_class = FeedbackInfoInputModelSerializer

class ListFeedbackInfoInputModelViewOneEntry(generics.RetrieveAPIView):

	queryset = FeedbackInfoInputModel.objects.all()
	lookup_url_kwarg = 'pk'
	serializer_class = FeedbackInfoInputModelSerializer

class DeleteListFeedbackInfoInputModelOneEntry(generics.RetrieveDestroyAPIView):

	queryset = FeedbackInfoInputModel.objects.all()
	lookup_url_kwarg = 'pk'
	serializer_class = FeedbackInfoInputModelSerializer

class UpdateListFeedbackInfoInputModelOneEntry(generics.RetrieveUpdateAPIView):

	queryset = FeedbackInfoInputModel.objects.all()
	lookup_url_kwarg = 'pk'
	serializer_class = FeedbackInfoInputModelSerializer