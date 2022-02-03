from django.urls import path

from contact_manager.views import CreateContact, ContactLists, ContactDelete, ContactUpdate

app_name = 'contact_manager'
urlpatterns = [
    path('create/', CreateContact.as_view(), name='create_contact'),
    path('contacts_list/', ContactLists.as_view(), name='contact_lists'),
    path('delete/<int:pk>', ContactDelete.as_view(), name='contact_delete'),
    path('update/<int:pk>', ContactUpdate.as_view(), name='contact_update'),
]

