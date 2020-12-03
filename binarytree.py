class Node():
    def __init__(self,data,right = None,left = None):
        self.data = data
        self.right = right
        self.left = left

class binary_tree():

    def __init__(self,root_val = None):

        # we will creat a root node for this instance of the tree
        if root_val:
            self.root = Node(root_val)

        # we will maintain a queue to traverse until we find an empty place
        self.queue = []


    def insert(self,val):
        '''
        we will do a level order insertion in the tree
        For level order insertion, like BFS, we will use a queue
        '''

        if not self.root:
            self.root = Node(self_val)
            self.queue = []

        else:
            # we need to add this at the start of every call because at every
            # call of insert, we pop root node from the queue

            self.queue.append(self.root)
            while(len(self.queue)):

                temp = self.queue[0]
                self.queue.pop(0)

                if not temp.left:
                    temp.left = Node(val)
                    break
                else:
                    self.queue.append(temp.left)

                if not temp.right:
                    temp.right = Node(val)
                    break
                else:
                    self.queue.append(temp.right)


    def levelorder(self):

        if not(self.root):
            return []

        result, current_level = [], [self.root]
        while current_level:
                next_level, vals = [] , []

                for node in current_level:
                        vals.append(node.data)
                        if node.left:
                            next_level.append(node.left)
                        if node.right:
                            next_level.append(node.right)

                current_level = next_level
                result.extend(vals)
        return result





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





Mytree = binary_tree(20)
Mytree.insert(10)
Mytree.insert(30)
Mytree.insert(40)
print(Mytree.levelorder())
Mytree.inorder()
Mytree.preorder()
Mytree.postorder()





















'''
----------------------------
*****CODE FROM THE NET*****
----------------------------
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data



    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(12)   # object of class node and the root node. All the insertion now will happen using this object
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()
'''
