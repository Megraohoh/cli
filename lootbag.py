
class Lootbag:

    def list_toys_for_child(self, child):
        return ["ball"]

    def get_toys_from_bag(self, child):
        return ["ball"]
    
    def add_toy_to_bag(self, toy):
        return toy

    def remove_toy_from_bag(self, toy):
        return toy  

    def assign_toy_to_child(self, child, toy):
        return (child, toy)
        
# Items can be added to bag, and assigned to a child.
# Items can be removed from bag, per child. Removing ball from the bag should not be allowed. A child's name must be specified.
# Must be able to list all children who are getting a toy.
# Must be able to list all toys for a given child's name.
# Must be able to set the delivered property of a child, which defaults to false to true.