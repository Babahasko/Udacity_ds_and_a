class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        start = self.root
        while start == None:
            if start.value < new_val:
                start = start.right
            if start.value > new_val:
                start = start.left
        start = Node(new_val)
        pass

    def search(self, find_val):
        start = self.root
        while start != None:
            if start.value == find_val:
                return True
            if start.value > find_val:
                start = start.right
            if start.value < find_val:
                start = start.left

        return False
        
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
