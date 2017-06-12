from django.test import TestCase
from .views import login_user,logout_user

class LoginTest(TestCase):
    def setUp(self):
        user = login_user.objects.create_user('temporary','temporary')

def test_login_user(self):
    c = login_user()
