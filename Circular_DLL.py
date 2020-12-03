'''

https://cppsecrets.com/users/109699104101114117107117114105109101103104971109749495564103109971051084699111109/Python-Program-to-Implement-Circular-Doubly-Linked-List.php

https://stackabuse.com/doubly-linked-list-with-python-examples/



'''



class Node:
    def __init__(self, data = 0,next = None, prev = None):
        self.data = data
        self.next = next
        self.previous = prev

class CircularDoublyLinkedList():
    def __init__(self):
        self.head = None
        self.count = 0


    def insert_at_end(self,data):
        node = Node(data)

        # if the current node is the first node
        if (not self.head):
            self.head = node
            node.next = node
            node.previous = node
            self.count+=1

        # if we already have nodes in the data
        else:
            curr_last_node = self.head.previous # self.head.previous points to the curr last node

            node.prev = curr_last_node
            node.next = curr_last_node.next
            curr_last_node.next = node
            self.head.previous = node

            self.count+=1

    def insert_at_start(self,data):
        node = Node(data)

        # if the current node is the first node
        if (not self.head):
            self.head = node
            node.next = node
            node.previous = node
            self.count+=1

        # if we already have nodes in the data
        else:
            curr_last_node = self.head.previous
            curr_first_node = self.head

            node.next = curr_first_node
            node.previous = curr_last_node
            curr_first_node.previous = node
            curr_last_node.next = node

            self.head = node
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





items = CircularDoublyLinkedList()
items.insert_at_end('PHP')
items.insert_at_end('Python')
items.insert_at_start('C#')
items.insert_at_start('C++')
items.insert_at_end('Java')
print(items.count)
print(items.traverse())
