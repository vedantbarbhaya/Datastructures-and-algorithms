'''

1. Traversal can begin from any node in the list. When the started node is visited
again, the list is meant to complete one cycle.

2. Used in Queue data structure implementation.

3.Circular Linked Lists is the basic idea for the round robin scheduling algorithm.

4. Circular Linked Lists are used majorly in time-sharing applications where the
operating system maintains a list of current users and must alternately allow each
user to use a small amount of CPU time (one user at a time). The operating system
will pick a user, allow him/her use a small amount of CPU time and then move to the
next user.
'''
class Node:
    def __init__(self, data = 0,next = None):
        self.data = data
        self.next = next

class Linked_List():
    def __init__(self):
        self.head = None
        self.count = 0


    def append(self,data):
        node = Node(data)


        # if the current node is the first node
        if (not self.head):
            self.head = node
            node.next = self.head
            self.count+=1

        # if we already have nodes in the data
        else:
            dummy = self.head
            while(dummy.next != self.head):
                dummy = dummy.next
            dummy.next = node
            node.next = self.head
            self.count+=1


    def traverse(self):
        dummy = self.head
        nodes = []

        while True:
            nodes.append(dummy.data)
            dummy = dummy.next
            if dummy == self.head:
                break

        return ("-->").join(nodes)

'''
    def remove(self):
        if self.count == 0:
            return "List is empty"
        else:
            print("\nremoved value = " + str(self.head.data))
            self.head = self.head.next
            self.count-=1
            if self.count==0:
                self.tail = None
'''





items =Linked_List()
items.append('PHP')
items.append('Python')
items.append('C#')
items.append('C++')
items.append('Java')
print(items.count)
print(items.traverse())
