from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Draw, DrawResult


class TestDraw(APITestCase):
    """Tests to validate the draw part of the API"""

    def setUp(self):
        """ Initialisation runned between every tests """
        self.Draw1 = {'id': 1, 'name': 'Draw1'}
        self.Draw2 = {'id': 2, 'name': 'Draw2'}
        self.Draw3 = {'id': 3, 'name': 'Draw3', 'draw_result': []}
        Draw.objects.create(**self.Draw1)
        Draw.objects.create(**self.Draw2)

    def test_get_draw_list(self):
        url = reverse('draws:draw-list')
        # send a GET request to the API to get the list of draw
        response = self.client.get(url, follow=True)
        # assert that the response status code is correct
        self.assertEqual(response.status_code, 200)
        # assert that the returned data is correct
        self.assertEqual(response.data[0]['name'], self.Draw1['name'])
        self.assertEqual(response.data[1]['name'], self.Draw2['name'])
    
    def test_post_draw(self):
        url = reverse('draws:draw-list')
        # send a POST request to the API with the new draw
        response = self.client.post(url, data=self.Draw3, format='json')
        # assert that the response status code is correct
        self.assertEqual(response.status_code, 201)
        # assert that the returned data is correct
        self.assertEqual(response.data['name'], self.Draw3['name'])

    def test_retrieve_draw(self):
        url = reverse('draws:draw-detail', kwargs={'draw_id': self.Draw1["id"]})
        # send a GET request to the API for an individual draw
        response = self.client.get(url)
        # assert that the response status code is correct
        self.assertEqual(response.status_code, 200)
        # assert that the returned data is correct
        self.assertEqual(response.data['name'], self.Draw1['name'])

    def test_destroy_draw(self):
        url = reverse('draws:draw-detail', kwargs={'draw_id': self.Draw1["id"]})
        # send a DELETE request to the API for an individual draw
        response = self.client.delete(url)
        # assert that the response status code is correct
        self.assertEqual(response.status_code, 204)
        url = reverse('draws:draw-list')
        # assert that the draw was not in the list of draw
        response = self.client.get(url)
        self.assertEqual(len(response.data),1)
        self.assertEqual(response.data[0]['name'], self.Draw2['name'])

    def test_get_draw_results(self):
        draw_result1 = {'id': 1, 'draw_id': 1, 'giver': "michel", 'receiver': "Renee"}
        DrawResult.objects.create(**draw_result1)
        url = reverse('draws:draw-draw_result-list', kwargs={'draw_id': self.Draw1["id"]})
        # send a GET request to the API to get the list of draw_result for the current draw
        response = self.client.get(url)
        # assert that the response status code is correct
        self.assertEqual(response.status_code, 200)
        # assert that the returned data is correct
        self.assertEqual(response.data[0]['giver'], draw_result1['giver'],)
        self.assertEqual(response.data[0]['receiver'], draw_result1['receiver'],)

    def test_post_draw_result(self):
        draw_result1 = {'id': 1, 'giver': "michel", 'receiver': "Renee"}
        url = reverse('draws:draw-draw_result-list', kwargs={'draw_id': self.Draw1["id"]})
        # send a POST request to the API with the data for the new draw_result
        response = self.client.post(url, data=draw_result1, format='json')
        # assert that the response status code is correct
        self.assertEqual(response.status_code, 201)
        # assert that the returned data is correct
        self.assertEqual(response.data['giver'], draw_result1['giver'],)
        self.assertEqual(response.data['receiver'], draw_result1['receiver'],)