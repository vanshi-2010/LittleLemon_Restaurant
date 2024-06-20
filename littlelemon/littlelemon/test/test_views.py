from django.test import TestCase
from restaurant.models import Booking, Menu
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class MenuItemsViewTests(APITestCase):

    def setUp(self):
        # Create a user and generate a token
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create menu items
        self.menu1 = Menu.objects.create(title="Item One", price=9.99, inventory=10)
        self.menu2 = Menu.objects.create(title="Item Two", price=19.99, inventory=10)

    def test_getall(self):
        url = '/restaurant/menu'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Item One')
        self.assertEqual(response.data[1]['title'], 'Item Two')

    def test_create_menu_item(self):
        url = '/restaurant/menu'
        data = {
            'title': 'Item Three',
            'price': 29.99,
            'inventory': 123
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 3)
        self.assertEqual(Menu.objects.last().title, 'Item Three')

    def test_retrieve_single_menu_item(self):
        url = f'/restaurant/menu/{self.menu1.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Item One')

    def test_update_single_menu_item(self):
        url = f'/restaurant/menu/{self.menu1.id}'
        data = {
            'title': 'Updated Item One',
            'price': 4.45,
            'inventory': 1
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.menu1.refresh_from_db()
        self.assertEqual(self.menu1.title, 'Updated Item One')

    def test_delete_single_menu_item(self):
        url = f'/restaurant/menu/{self.menu1.id}'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 1)

    def test_unauthenticated_access(self):
        self.client.credentials()  # Remove the token
        url = '/restaurant/menu'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        

class BookingViewSetTests(APITestCase):

    def setUp(self):
        # Create a user and generate a token
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create some sample data
        self.booking1 = Booking.objects.create(name='Booking One', no_of_guests=2, booking_date='2024-06-18T12:00:00Z')
        self.booking2 = Booking.objects.create(name='Booking Two', no_of_guests=4, booking_date='2024-06-19T12:00:00Z')

        
    def test_list_bookings(self):
        url = '/restaurant/booking/tables'  # Specify the URL directly
        response = self.client.get(url)
        # print(response.data)  # Print response data for debugging
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)    

    def test_retrieve_booking(self):
        url = f'/restaurant/booking/tables/{self.booking1.id}'  # Specify the URL directly
        response = self.client.get(url)
        # print(response.data)  # Print response data for debugging
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Booking One')

    def test_create_booking(self):
        url = '/restaurant/booking/tables'  # Specify the URL directly
        data = {
            'name': 'Booking Three',
            'no_of_guests': 3,
            'booking_date': '2024-06-20T12:00:00Z'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 3)
        self.assertEqual(Booking.objects.last().name, 'Booking Three')

    def test_update_booking(self):
        url = f'/restaurant/booking/tables/{self.booking1.id}'  # Specify the URL directly
        data = {
            'name': 'Updated Booking One',
            'no_of_guests': 5,
            'booking_date': '2024-06-21T12:00:00Z'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.booking1.refresh_from_db()
        self.assertEqual(self.booking1.name, 'Updated Booking One')
        self.assertEqual(self.booking1.no_of_guests, 5)

    def test_delete_booking(self):
        url = f'/restaurant/booking/tables/{self.booking1.id}'  # Specify the URL directly
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 1)

    def test_unauthenticated_access(self):
        self.client.credentials()  # Remove the token
        url = '/restaurant/booking/tables'  # Specify the URL directly
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
