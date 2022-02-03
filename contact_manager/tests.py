from django.test import TestCase, RequestFactory
from django.urls import reverse
from.views import CreateContact, ContactLists
from .models import Contact

# Create your tests here.

class TestCreateView(TestCase):
    def test_create_view_response(self):
        self.factory = RequestFactory()
        request = self.factory.get('http://127.0.0.1:8000/contacts/create/')
        response = CreateContact.as_view()(request)
        self.assertEqual(response.status_code, 200)



class TestListView(TestCase):
    def test_contactlists_view_response(self):
        self.factory = RequestFactory()
        request = self.factory.get('http://127.0.0.1:8000/contacts/contacts_list/')
        response = ContactLists.as_view()(request)
        self.assertEqual(response.status_code, 200)


class TestUpdateView(TestCase):
    def test_update_view_response(self):
        contact = Contact.objects.create(fullname="Ahmad Khakpour", phone_number="09152357489", email_address="Ahmadkh2020@gmail.com")

        response = self.client.post(
            reverse('contact_manager:contact_update', kwargs={'pk': contact.id}), 
            {'fullname': 'Ahmad Khakpour', 'phone_number': '09152357489', 'email_address': 'Ahmadkh2020@gmail.com'})

        self.assertEqual(response.status_code, 302)

        contact.refresh_from_db()
        self.assertEqual(contact.phone_number, '09152357489')


class TestDeleteView(TestCase):
    def test_delete_view_response(self):
        contact = Contact.objects.create(fullname="Alireza Khakpour", phone_number="09152357490", email_address="Alireza1920@gmail.com")

        response = self.client.get(reverse('contact_manager:contact_delete', args=(contact.id,)), follow=True)
        self.assertContains(response, 'Are you sure you want to delete') 

        post_response = self.client.post(reverse('contact_manager:contact_delete', args=(contact.id,)), follow=True)
        self.assertRedirects(post_response, reverse('contact_manager:contact_lists'), status_code=302)

