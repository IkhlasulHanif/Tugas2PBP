from urllib import response
from django.test import TestCase, override_settings
from django.urls import reverse
@override_settings(STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage')


# Create your tests here.
class MyWatchListTest(TestCase):

    def test_url_json(self):
        response = self.client.get(reverse('mywatchlist:show_json'))
        self.assertEquals(response.status_code, 200)

    def test_url_xml(self):
        response = self.client.get(reverse('mywatchlist:show_xml'))
        self.assertEquals(response.status_code, 200)

    def test_url_html(self):
        response = self.client.get(reverse('mywatchlist:show_mywatchlist'))
        self.assertEquals(response.status_code, 200)