from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import HomeView


class TestCoreUrls(SimpleTestCase):
    
    #test de url home
    def test_home_url_resolves(self):
        url=reverse("home")
        self.assertEquals(resolve(url).func.view_class, HomeView)