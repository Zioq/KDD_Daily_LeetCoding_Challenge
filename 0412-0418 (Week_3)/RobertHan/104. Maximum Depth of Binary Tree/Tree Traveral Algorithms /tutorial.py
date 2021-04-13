# This code for the Binray Tree Traversal Algorithm(BFS)

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)

    def print_tree(self, travalsal_type):
        if travalsal_type == 'preorder':
            return self.preorder_print(tree.root, "")
        elif travalsal_type == 'inorder':
            return self.inorder_print(tree.root, "")
        elif travalsal_type == 'postorder':
            return self.postorder_print(tree.root, "")
        else:
            print("Traversal type"+ str(travalsal_type)+ "is not supported")
            return False

    def preorder_print(self, start, traversal):
        """ Node(Root)->Left->Right """
        if start:
            traversal += (str(start.value) +"-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self,start, traversal):
        """ Left->Node(root)->Right """
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) +"-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self,start, traversal):
        """ Left->Right->Node(root) """
        if start:
            traversal = self.postorder_print(start.left,traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) +"-")
        return traversal



#           1
#          /   \
#         2     3
#       /  |    / \
#      4    5  6  7

# Set up tree:
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


"""[Pre-Order Traversal] : n->l->r
1. Check if the current node is null
2. Display the data part of the root(or current node)
3. Traverse the left subtree by recursively calling the pre-order function
4. Traverse the right subtree by recursively claling the pre-order function.

"""
print(tree.print_tree('preorder'))
print(tree.print_tree('inorder'))
print(tree.print_tree('postorder'))