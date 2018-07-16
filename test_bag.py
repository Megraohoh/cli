import unittest
from lootbag import Lootbag


class TestLootBag(unittest.TestCase):
# get something from bag
    def test_get_all_childs_toys_from_bag(self):
        lootbag = Lootbag()
        result = lootbag.get_toys_from_bag("suzy")
        expected = ["ball"]
        self.assertEqual(result, expected)

    def test_toy_added_to_bag(self):
        lootbag = Lootbag()
        result = lootbag.add_toy_to_bag("rope")
        # will return argument 
        expected = ("rope")
        self.assertEqual(result, expected) 

    # def test_toy_assigned_to_child(self):
    #     self.assertTrue(child, Lootbag)  

if __name__ == '__main__':
    unittest.main()          