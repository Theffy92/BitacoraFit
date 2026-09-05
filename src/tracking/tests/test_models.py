from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from ..models import WeightEntry
from decimal import Decimal

# Create your tests here.
class WeightEntryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.date = timezone.now().date()

    def test_create_weight_entry(self):
        entry = WeightEntry.objects.create(
            user=self.user,
            date=self.date,
            weight=Decimal('150.75'),
            notes='Felt good today!'
        )
        self.assertEqual(entry.weight, Decimal('150.75'))
        self.assertEqual(str(entry), f"testuser - {self.date}: 150.75 lbs")

    def test_weight_entry_without_notes(self):
        entry = WeightEntry.objects.create(
            user=self.user,
            date=self.date,
            weight=Decimal('150.75')
        )
        self.assertIsNone(entry.notes)