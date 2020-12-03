    '''
Linked lists, when compared to lists, are much more straightforward when it comes to
insertion and deletion of elements at the beginning or end of a list, where their
time complexity is always constant: O(1).

For this reason, linked lists have a performance advantage over normal lists when
implementing a queue (FIFO), in which elements are continuously inserted and
removed at the beginning of the list. But they perform similarly to a list when
implementing a stack (LIFO), in which elements are inserted and removed at the
end of the list.

By using head and tail pointer, inserting at either ends becomes an O(1) operation
whereas in removal, removal from beginning is O(1) but removal from end is still
an O(n) operation.
'''



'''
                IMPLEMENTING QUEUE(FIFO) USING LINKED LISTS
A new node is always inserted in the end using the tail pointer and
the node being deleted is always from the start(which is the first node to be
inserted) using the head pointer.

Head points to the first node inserted and tail points to the last node inserted.
'''

class Node:
    def __init__(self, data = 0,next = None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0


    def append(self,data):
        node = Node(data)

        # if we already have nodes in the data
        if self.head:
            self.tail.next = node
            self.tail = node
            self.count+=1

        # if the current node is the first node
        else:
            self.tail = node
            self.head = node
            self.count+=1

    def remove(self):
        if self.count == 0:
            return "List is empty"
        else:
            print("\nremoved value = " + str(self.head.data))
            self.head = self.head.next
            self.count-=1

            # if we have deleted the last element, head bcoz of self.head = self.head.next
            # will already be None so we need to set tail = None
            if self.count==0:
                self.tail = None



    def traverse(self):
        dummy = self.head # so now dummy refers to the first node
        nodes = []
        while dummy:
            nodes.append(dummy.data)
            dummy = dummy.next
        return ("-->").join(nodes)



items =Linked_List()
items.append('PHP')
items.append('Python')
items.append('C#')
items.append('C++')
items.append('Java')

print(items.traverse())
items.remove()




'''
                IMPLEMENTING STACK(FILO) USING LINKED LISTS
For that we need to insert the new node always at the beginning so that while
removing, we can remove from beginning and achieve FILO.

Here head points to the last node inserted and tail points to the first node inserted
'''
class Node:
    def __init__(self, data = 0,next = None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0


    def append(self,data):
        node = Node(data)
        if self.head:
            node.next = self.head
            self.head = node
            self.count+=1
        else:
            self.tail = node
            self.head = node
            self.count+=1

    def remove(self):
        if self.count == 0:

            return "List is empty"
        else:
            print("\nremoved value = " + str(self.head.data))
            self.head = self.head.next
            self.count-=1
            if self.count==0:
                self.tail = None


    def traverse(self):
        dummy = self.head
        nodes = []
        while dummy:
            nodes.append(dummy.data)
            dummy = dummy.next
        return ("-->").join(nodes)



items =Linked_List()
items.append('PHP')
items.append('Python')
items.append('C#')
items.append('C++')
items.append('Java')

items.traverse()
items.remove()
