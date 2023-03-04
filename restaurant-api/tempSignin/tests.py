from django.test import TestCase
from django.utils import timezone
from .models import tempUser


class TempUserTestCase(TestCase):
    def setUp(self):
        tempUser.objects.create(name="John Doe", email="johndoe@example.com")

    def test_tempUser_expiration_date(self):
        """
        Test that the expiration date is correctly set to 15 minutes from the creation date
        """
        user = tempUser.objects.get(name="John Doe")
        expiration_time = user.expiration - user.created
        self.assertAlmostEqual(expiration_time.seconds, 900, delta=10)
