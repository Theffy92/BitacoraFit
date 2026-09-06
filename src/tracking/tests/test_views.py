from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from decimal import Decimal

from tracking.models import WeightEntry


class TrackingViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test-user",
            password="test-password",
        )
        self.client.force_login(self.user)

    def test_dashboard_redirects_unauthenticated_users_to_login(self):
        self.client.logout()

        response = self.client.get(reverse("weight_dashboard"))

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('weight_dashboard')}",
        )

    def test_dashboard_shows_only_current_users_entries(self):
        other_user = get_user_model().objects.create_user(
            username="other-user",
            password="other-password",
        )
        current_entry = WeightEntry.objects.create(
            user=self.user,
            date="2026-09-05",
            weight=Decimal("150.75"),
        )
        WeightEntry.objects.create(
            user=other_user,
            date="2026-09-06",
            weight=Decimal("180.25"),
        )

        response = self.client.get(reverse("weight_dashboard"))

        self.assertEqual(response.context["latest_entry"], current_entry)
        self.assertEqual(list(response.context["recent_entries"]), [])

    def test_log_weight_creates_entry_for_current_user(self):
        response = self.client.post(
            reverse("log_weight"),
            {
                "date": "2026-09-05",
                "weight": "150.75",
                "notes": "Felt good today!",
            },
        )

        self.assertRedirects(response, reverse("weight_dashboard"))
        entry = WeightEntry.objects.get()
        self.assertEqual(entry.user, self.user)
        self.assertEqual(entry.weight, Decimal("150.75"))
        self.assertEqual(entry.notes, "Felt good today!")

    def test_dashboard_with_zero_entries(self):
        response = self.client.get(reverse("weight_dashboard"))

        self.assertIsNone(response.context["latest_entry"])
        self.assertEqual(list(response.context["recent_entries"]), [])

    def test_dashboard_with_one_entry(self):
        entry = WeightEntry.objects.create(
            user=self.user,
            date="2026-09-05",
            weight=Decimal("150.75"),
        )

        response = self.client.get(reverse("weight_dashboard"))

        self.assertEqual(response.context["latest_entry"], entry)
        self.assertEqual(list(response.context["recent_entries"]), [])

    def test_dashboard_with_multiple_entries(self):
        oldest_entry = WeightEntry.objects.create(
            user=self.user,
            date="2026-09-03",
            weight=Decimal("152.00"),
        )
        latest_entry = WeightEntry.objects.create(
            user=self.user,
            date="2026-09-05",
            weight=Decimal("150.75"),
        )

        response = self.client.get(reverse("weight_dashboard"))

        self.assertEqual(response.context["latest_entry"], latest_entry)
        self.assertEqual(list(response.context["recent_entries"]), [oldest_entry])

class WeightHistoryViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test-user",
            password="test-password",
        )
        self.client.force_login(self.user)
    
    def test_weight_history_shows_only_current_users_entries(self):
        other_user = get_user_model().objects.create_user(
            username="other-user",
            password="other-password",
        )
        current_entry = WeightEntry.objects.create(
            user=self.user,
            date="2026-09-05",
            weight=Decimal("150.75"),
        )
        WeightEntry.objects.create(
            user=other_user,
            date="2026-09-06",
            weight=Decimal("180.25"),
        )

        response = self.client.get(reverse("weight_history"))

        self.assertIn(current_entry, response.context["weight_entries"])
        self.assertNotIn(WeightEntry.objects.get(user=other_user), response.context["weight_entries"])
