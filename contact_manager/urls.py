from django.urls import include, path

from contact_manager.views import ContactViewSet, CreateContact, ContactLists, ContactDelete, ContactUpdate
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet)


app_name = 'contact_manager'
urlpatterns = [
    path('create/', CreateContact.as_view(), name='create_contact'),
    path('contacts_list/', ContactLists.as_view(), name='contact_lists'),
    path('delete/<int:pk>', ContactDelete.as_view(), name='contact_delete'),
    path('update/<int:pk>', ContactUpdate.as_view(), name='contact_update'),
]

urlpatterns += [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

