# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from gym.models import *

class GymTest(APITestCase):
    def test_create_gym(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('gym')
        data = {'username':'gogym','title': 'GO-Gym','email': 'example@example.com','code':'north01','status':False}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Gym.objects.count(), 1)
        self.assertEqual(Gym.objects.get().name, 'GO-Gym')
        self.assertEqual(Gym.objects.get().status, False)


    def test_update_gym(self):
        """
        Ensure we can update object.
        """
        url = reverse('gym')
        #creste gym first
        data = {'name': 'GO-Gym','email': 'example@example.com','code':'north01','status':False}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        Gym1 = Gym.objects.get(id=1)

        data = {'name': 'RED-Gym','email': 'example2@example.com','code':'north02','status':True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #update gym details
        data = {'id':2,'name': 'BLUE-One-Gym','code':'north02','status':True}
        response = self.client.put(url, data, format='json')
        #get gym after update
        Gym2 = Gym.objects.get(id=2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Gym2.id, 2)
        self.assertEqual(Gym2.name, 'BLUE-One-Gym')
        self.assertEqual(Gym2.status, True)

        url = reverse('gym',kwargs={'id': '1'})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Gym1.id, 1)
        self.assertEqual(Gym1.name, 'GO-Gym')
        self.assertEqual(Gym1.status, False)

    def test_delete_gym(self):
        """
        Ensure we can delete object.
        """
        url = reverse('gym')
        #creste gym first
        data = {'name': 'GO-Gym','email': 'example@example.com','code':'north01','status':False}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #update gym details
        data = {'id':1}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_gym(self):
        """
        Ensure we can list all object.
        """
        url = reverse('gym')
        #creste gym first
        data = {'name': 'GO-Gym','email': 'example@example.com','code':'north01','status':False}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = {'name': 'RED-Gym','email': 'example2@example.com','code':'north02','status':True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #list gyms
        url = reverse('gyms')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Gym.objects.count(), 2)

