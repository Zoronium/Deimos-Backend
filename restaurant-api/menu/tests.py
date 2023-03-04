from django.test import TestCase

# Create your tests here.

from .models import Category, Menu


class MenuTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Appetizers")
        self.menu_item = Menu.objects.create(
            name="Mozzarella Sticks",
            description="Fried cheese sticks with marinara sauce",
            price=8,
            category=self.category,
        )

    def test_menu_item_str(self):
        """
        Test that the string representation of the menu item is correct
        """
        self.assertEqual(str(self.menu_item), "Mozzarella Sticks")

    def test_menu_item_category(self):
        """
        Test that the menu item is assigned to the correct category
        """
        self.assertEqual(self.menu_item.category, self.category)

    def test_menu_item_price(self):
        """
        Test that the menu item price is greater than zero
        """
        self.assertGreater(self.menu_item.price, 0)
