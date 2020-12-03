class Node():

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

class BST():

    def __init__(self,root_val = None):
        if root_val:
            self.root = Node(val)

    #def root(val):
    #    if  not self.root:
    #        self.root = Node(val)
    #    else:
    #        print('Root is already defined. Please use BST.insert() method to add elements to the tree')

    def insert(self,val):

        def helper(temp,val):
            if val > temp.data:
                if temp.right is None:
                        temp.right = Node(val)
                else:
                        helper(temp.right,val)

            elif val < temp.data:
                if temp.left is None:
                        temp.left = Node(val)
                else:
                        helper(temp.left, val)

        if not self.root:
            self.root = Node(val)
        else:
            helper(self.root,val)

    def inorder(self):
         '''
         we will do an inorder traversal of the tree
         '''
         def traversal(temp):

             if not temp:
                 return

             traversal(temp.left)
             print(temp.data,end = " ")
             traversal(temp.right)

         print("\n")
         print("INORDER OF THE TREE")
         traversal(self.root)

    def preorder(self):
         '''
         we will do an inorder traversal of the tree
         '''
         def traversal(temp):

             if not temp:
                 return

             print(temp.data,end = " ")
             traversal(temp.left)
             traversal(temp.right)

         print("\n")
         print("PREORDER OF THE TREE")
         traversal(self.root)

    def postorder(self):
         '''
         we will do an inorder traversal of the tree
         '''
         def traversal(temp):

             if not temp:
                 return

             traversal(temp.left)
             traversal(temp.right)
             print(temp.data,end = " ")

         print("\n")
         print("POSTORDER OF THE TREE")
         traversal(self.root)


bst_tree = BST(25)
bst_tree.insert(14)
bst_tree.insert(27)
bst_tree.insert(17)
bst_tree.insert(10)
bst_tree.insert(34)
bst_tree.insert(26)
bst_tree.inorder()
