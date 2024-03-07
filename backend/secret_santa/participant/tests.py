from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Participant, Blacklist
from .serializers import ParticipantSerializer


class TestParticipant(APITestCase):
    """Tests to validate the participant part of the API"""

    def setUp(self):
        """ Initialisation runned between every tests """
        self.michel = {'id': 1, 'first_name': 'Michel', 'last_name': 'Dupond'}
        self.georges = {'id': 2,'first_name': 'Georges', 'last_name': 'Alves'}
        self.giselle = {'id': 3, 'first_name': 'Giselle', 'last_name': 'Marie'}
        Participant.objects.create(**self.michel)
        Participant.objects.create(**self.georges)

    def test_get_participant_list(self):
        url = reverse('participants:participant-list')
        # send a GET request to the API to get the list of participant
        response = self.client.get(url, follow=True)
        # assert that the response status code is correct
        self.assertEqual(response.status_code, 200)
        self.michel['blacklist']= []
        self.georges['blacklist']= []
        # assert that the returned data is correct
        self.assertEqual(response.data, ParticipantSerializer([self.michel, self.georges], many=True).data)

    def test_post_participant(self):
        url = reverse('participants:participant-list')
        # send a POST request to the API with the new participant
        response = self.client.post(url, data=self.giselle, format='json')
        # assert that the response status code is correct
        self.assertEqual(response.status_code, 201)
        # assert that the returned data is correct
        self.giselle['blacklist']= []
        self.assertEqual(response.data, ParticipantSerializer(self.giselle).data)

    def test_retrieve_participant(self):
        url = reverse('participants:participant-detail', kwargs={'participant_id': self.georges["id"]})
        # send a GET request to the API for an individual participant
        response = self.client.get(url)
        # assert that the response status code is correct
        self.assertEqual(response.status_code, 200)
        self.georges['blacklist']= []
        # assert that the returned data is correct
        self.assertEqual(response.data, ParticipantSerializer(self.georges).data)

    def test_destroy_participant(self):
        url = reverse('participants:participant-detail', kwargs={'participant_id': self.michel["id"]})
        # send a DELETE request to the API for an individual participant
        response = self.client.delete(url)
        # assert that the response status code is correct
        self.assertEqual(response.status_code, 204)
        url = reverse('participants:participant-list')
        # assert that the participant was not in the list of participant
        response = self.client.get(url)
        self.assertNotIn(self.michel, response.data)

    def test_get_blacklist(self):
        michel_blacklist_georges = {'id': 1, 'owner_id': 1, 'blacklisted_id': 2}
        Blacklist.objects.create(**michel_blacklist_georges)
        url = reverse('participants:participant-blacklist-list', kwargs={'participant_id': self.michel["id"]})
        # send a GET request to the API to get the list of blacklisted for the current participant
        response = self.client.get(url)
        # assert that the response status code is correct
        self.assertEqual(response.status_code, 200)
        # assert that the returned data is correct
        self.assertEqual(response.data[0]['id'], michel_blacklist_georges['id'])

    def test_post_blacklist(self):
        michel_blacklist_georges = {'id': 1, 'blacklisted': 2}
        url = reverse('participants:participant-blacklist-list', kwargs={'participant_id': self.michel["id"]})
        # send a POST request to the API with the data for the new blacklisted
        response = self.client.post(url, data=michel_blacklist_georges, format='json')
        # assert that the response status code is correct
        self.assertEqual(response.status_code, 201)
        # assert that the returned data is correct
        self.assertEqual(response.data, michel_blacklist_georges)

    def test_destroy_blacklist(self):
        michel_blacklist_georges = {'id': 1, 'owner_id': 1, 'blacklisted_id': 2}
        Blacklist.objects.create(**michel_blacklist_georges)
        url = reverse('participants:participant-blacklist-detail',
                      kwargs={'participant_id': self.michel["id"],
                              'blacklist_id': michel_blacklist_georges["id"]})
        # send a DELETE request to the API for a blacklisted
        response = self.client.delete(url)
        # assert that the response status code is correct
        self.assertEqual(response.status_code, 204)
        url = reverse('participants:participant-blacklist-list', kwargs={'participant_id': self.michel["id"]})
        # assert that the blacklist is empty as expected
        response = self.client.get(url)
        self.assertEqual([], response.data)