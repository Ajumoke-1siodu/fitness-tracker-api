from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from activities.models import Activity

User = get_user_model()

class ActivityTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="geo", password="pass123")
        self.client.login(username="geo", password="pass123")
        self.list_url = reverse("activity-list")
        self.summary_url = reverse("activity-summary")

    def test_create_activity(self):
        payload = {
            "type": "running",
            "date": "2025-12-20",
            "duration_minutes": 45,
            "distance_km": 8.2,
            "calories": 520,
        }
        res = self.client.post(self.list_url, payload, format="json")
        self.assertEqual(res.status_code, 201)
        self.assertEqual(Activity.objects.count(), 1)
        self.assertEqual(Activity.objects.first().user, self.user)

    def test_filter_by_date_range(self):
        Activity.objects.create(user=self.user, type="running", date="2025-12-10", duration_minutes=30)
        Activity.objects.create(user=self.user, type="running", date="2025-12-20", duration_minutes=60)
        res = self.client.get(self.list_url + "?date_from=2025-12-15&date_to=2025-12-22")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data["results"]), 1)

    def test_summary_month(self):
        Activity.objects.create(user=self.user, type="cycling", date="2025-12-05", duration_minutes=50, distance_km=15, calories=400)
        res = self.client.get(self.summary_url + "?period=month")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["totals"]["duration_minutes"], 50)

