from django.test import TestCase
from restaurant.serializers import MenuSerializer
# Create your tests here.
from restaurant.models import MenuItem

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = MenuItem.objects.create(title="IceCream",price=80,inventory=100)
        self.menu2 = MenuItem.objects.create(title="Chiken",price=2000,inventory=50)
        
    def test_getall(self):
        # Retrieve all Menu objects
        menus = MenuItem.objects.all()

        # Serialize the retrieved objects
        serializer = MenuSerializer(menus, many=True)
        serialized_data = serializer.data

        # Get the expected serialized data
        expected_data = [
            {"name": self.menu1.title, "description": self.menu1.price},
            {"name": self.menu2.title, "description": self.menu2.price},
        ]

        # Assert that the serialized data matches the expected data
        self.assertEqual(serialized_data, expected_data)