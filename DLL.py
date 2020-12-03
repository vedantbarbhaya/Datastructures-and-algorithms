'''
With doubly linked lists, we are capable of inserting or deleting elements
from both ends of a queue with constant O(1) performance.
'''

class Node:
    def __init__(self, data = 0,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0


    def append(self, data, pos = "E"):
        node = Node(data)

        if pos == "S":

            if self.head:
                self.head.prev,node.next  = node, self.head
                self.head = node
                self.count+=1
            else:
                self.tail = node
                self.head = node
                self.count+=1

        if pos == "E":

            if self.head:
                self.tail.next,node.prev  = node, self.tail
                self.tail = self.tail.next

                self.count+=1
            else:
                self.tail = node
                self.head = node
                self.count+=1

    def remove(self,pos = "E"):
        if self.count == 0:
            return "List is empty"

        if pos == 'E':

            print("removed value = " + str(self.tail.data))
            self.tail = self.tail.prev
            self.tail.next = None
            self.count-=1
            if self.count==0:
                self.head = None
                self.tail = None

        if pos == 'S':

            print("removed value = " + str(self.head.data))
            self.head = self.head.next
            self.count-=1
            if self.count==0:
                self.head = None
                self.tail = None



    def traverse(self,pos = "S"):
        if pos == "S":
            dummy = self.head
            nodes = []
            while dummy:
                nodes.append(dummy.data)
                #print(dummy.data)
                dummy = dummy.next
                print("im here")
            return ("-->").join(nodes)

        if pos == "E":
            dummy = self.tail
            nodes = []
            while dummy:
                nodes.append(dummy.data)
                dummy = dummy.prev

            return ("-->").join(nodes)


items = DLL()
items.append('PHP',)
items.append('Python',"S")
items.append('C#')
items.append('C++')
items.append('Java')
print(items.traverse(""))
