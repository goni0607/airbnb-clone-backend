from rest_framework.test import APITestCase
from . import models
from users.models import User


class TestAmenities(APITestCase):

    NAME = "Amenity Test"
    DESC = "Amenity Description"
    URL = "/api/v1/rooms/amenities/"

    def setUp(self) -> None:
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_all_amenities(self):
        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200"
        )

        self.assertIsInstance(
            data,
            list
        )

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], self.NAME)
        self.assertEqual(data[0]["description"], self.DESC)

    def test_create_amenity(self):
        new_amenity_name = "New Amenity"
        new_amenity_desc = "New Amenity Description"

        response = self.client.post(
            self.URL,
            data={"name": new_amenity_name,
                  "description": new_amenity_desc},
        )
        data = response.data
        self.assertEqual(response.status_code, 200, "Status code isn't 200")
        self.assertEqual(data["name"], new_amenity_name)
        self.assertEqual(data["description"], new_amenity_desc)


class TestRooms(APITestCase):

    def setUp(self):
        user = User.objects.create(
            username="test",
        )
        user.set_password("123")
        user.save()
        self.user = user

    def test_create_room(self):
        response = self.client.post("/api/v1/rooms/")
        self.assertEqual(response.status_code, 403)

        self.client.force_login(self.user)
        # self.client.login(
        #     username="test",
        #     password="123",
        # )

        response = self.client.post("/api/v1/rooms/")
        print(response.json())
