from django.test import TestCase, Client

# Create your tests here.


class ThomasMurrayEndpointTest(TestCase):

    def test_currency(self):
        """
        Test that we can get USD/EUR exchange rate
        """
        client = Client()

        response = client.get('/api/currency/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data['data'], None)

    def test_ip(self):
        """
        Test that we can get ip address of server
        """
        client = Client()

        response = client.get('/api/ip/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data['data'], None)