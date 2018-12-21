from django.urls import path
from .views import (home,list_entries, emailfetch ,ContentAutoComplete ,findstatusofid,detailspage,list_entries_for_site, ListFeedbackInfoInputModelView, ListFeedbackInfoInputModelViewOneEntry,
 DeleteListFeedbackInfoInputModelOneEntry, UpdateListFeedbackInfoInputModelOneEntry)


urlpatterns = [

path('', home, name='fbscreen-home'),
path('findstatusofid',findstatusofid, name='findstatus'),
path('content-autocomplete', ContentAutoComplete.as_view(),name='content-autocomplete'),
path('listentries',list_entries, name='list-entries'),
path('emailfetch',emailfetch, name='email-fetch'),
path('listentries/listentriesforsite',list_entries_for_site ,name='listentriesforsite'),
path('listapis/<int:pk>/details', detailspage ,name='details-page'),
# path('apidetail/<int:pk>',PostDetailView.as_view(),name='api-detail'),
path('listapis', ListFeedbackInfoInputModelView.as_view(),name='model-all'),
path('listapis/<int:pk>', ListFeedbackInfoInputModelViewOneEntry.as_view(), name='model-one-entry'),
path('listapis/<int:pk>/delete', DeleteListFeedbackInfoInputModelOneEntry.as_view(), name='delete-one-entry'),
path('listapis/<int:pk>/update', UpdateListFeedbackInfoInputModelOneEntry.as_view(), name='update-one-entry')

]