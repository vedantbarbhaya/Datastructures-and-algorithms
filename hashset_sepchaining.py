
'''
*************************************************
HASHSET WITH SEPERATE CHAINING FOR COLLISION DETECTION
*************************************************
'''

'''
*************************************************
 HASHSET USING LINKEDLIST FOR COLLISION DETECTION
*************************************************
'''
class LinkedList():

        def __init__(self,value = 0,next = None):
            self.value = value
            self.next = next

        def add(self,value):
            '''
            traverses the list to find the value passed and adds it at the first
            avaiable node in the Linkedlist
            '''
            found = True
            if self.next == None:
                self.value = value
                print("value added in the first node")
                self.next = LinkedList()


            else:
                temp = self
                while(temp.next != None):

                    if temp.value == value:
                        print("value already exists")
                        found = True
                        break

                    temp = temp.next

                if found == False:
                    print("Linked list extended")
                    temp.value = value
                    temp.next = LinkedList()
                    print("value added")

        def remove(self, value):
            '''
            traverses the list to find the value passed and removes it from the
            Linkedlist
            '''
            temp = self
            while(temp.next!=None):
                if temp.value == value:
                    temp.value = 0
                    temp.next = None
                    print("value removed")
                    return None
                temp = temp.next
            print("Value not found")



        def get(self,value):

            temp = self

            while(temp.next!=None):
                if temp.value == value:
                    return True
                temp = temp.next
            return False




class MyHashSet():

    def __init__(self):
        '''
        key_space =  modulo base
        hash_table = list of objects of class LinkedList
        '''

        self.key_space = 769
        self.hash_table = [LinkedList() for i in range(self.key_space)]

    def add(self,value):
        hash_key = value % self.key_space
        self.hash_table[hash_key].add(value)

    def remove(self,value):
        hash_key =  value % self.key_space
        self.hash_table[hash_key].remove(value)

    def contains(self, value):
        hash_key= value %self.key_space
        return self.hash_table[hash_key].get(value)



'''
*************************************************
 HASHSET USING LIST FOR COLLISION DETECTION
 ************************************************
 '''
class Bucket():

    def __init__(self):
          self.bucket=[]

    def update(self, key):
        found=False
        for i,k in enumerate(self.bucket):
            if key==k:
                self.bucket[i]=key
                found=True
                break

        if not found:
            self.bucket.append(key)

    def get(self, key):
        for k in self.bucket:
            if k==key:
                return True
        return False

    def remove(self, key):
          for i,k in enumerate(self.bucket):
             if key==k:
                del self.bucket[i]

class MyHashSet:

    def __init__(self):
        self.key_space = 2096
        self.hash_table=[Bucket() for i in range(self.key_space)]

    def add(self, key):
        hash_key=key%self.key_space
        self.hash_table[hash_key].update(key)

    def remove(self, key):
        hash_key=key%self.key_space
        self.hash_table[hash_key].remove(key)

    def contains(self, key):
        hash_key=key%self.key_space
        return self.hash_table[hash_key].get(key)
