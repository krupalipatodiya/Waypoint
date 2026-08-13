from django.test import TestCase
from django.urls import reverse

from .models import Trail


class TrailModelTests(TestCase):

    def test_trail_string_returns_name(self):
        trail = Trail.objects.create(
            name="Test Trail",
            distance_km=5.50,
            elevation_gain=100,
            difficulty="easy",
            is_open=True,
        )

        self.assertEqual(str(trail), "Test Trail")


class TrailCatalogTests(TestCase):

    def setUp(self):
        Trail.objects.create(
            name="Short Trail",
            distance_km=3.00,
            elevation_gain=80,
            difficulty="easy",
            is_open=True,
        )

        Trail.objects.create(
            name="Long Trail",
            distance_km=10.00,
            elevation_gain=300,
            difficulty="hard",
            is_open=True,
        )

        Trail.objects.create(
            name="Closed Trail",
            distance_km=5.00,
            elevation_gain=150,
            difficulty="moderate",
            is_open=False,
        )

    def test_catalog_page_loads(self):
        response = self.client.get(reverse("catalog"))

        self.assertEqual(response.status_code, 200)

    def test_open_trails_appear(self):
        response = self.client.get(reverse("catalog"))

        self.assertContains(response, "Short Trail")
        self.assertContains(response, "Long Trail")

    def test_closed_trails_do_not_appear(self):
        response = self.client.get(reverse("catalog"))

        self.assertNotContains(response, "Closed Trail")

    def test_trails_are_ordered_by_distance(self):
        response = self.client.get(reverse("catalog"))

        trails = list(response.context["trails"])

        self.assertEqual(trails[0].name, "Short Trail")
        self.assertEqual(trails[1].name, "Long Trail")