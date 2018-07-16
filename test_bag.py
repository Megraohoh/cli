import unittest
from lootbag import Lootbag


class TestLootBag(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bag = Lootbag()

    def test_can_list_toys_from_bag_for_child(self):
        toy = "ball"
        mikey_toys = self.bag.list_toys_for_child("Mikey")
        self.assertIn(toy, mikey_toys)

    def test_get_all_childs_toys_from_bag(self):
        lootbag = Lootbag()
        result = lootbag.get_toys_from_bag("suzy")
        expected = ["ball"]
        self.assertEqual(result, expected)

    def test_toy_added_to_bag(self):
        lootbag = Lootbag()
        result = lootbag.add_toy_to_bag("rope")
        # will return argument 
        expected = "rope"
        self.assertEqual(result, expected) 

    def test_toy_removed_from_bag(self):
        lootbag = Lootbag()
        result = lootbag.remove_toy_from_bag("ball")
        expected = "ball"
        self.assertEqual(result, expected)

    def test_toy_assigned_to_child(self):
        lootbag = Lootbag()  
        result = lootbag.assign_toy_to_child("suzy", "ball")
        expected = ("suzy", "ball")
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()          