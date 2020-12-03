'''
This is a circular queue code
For conceptual understanding, refer - https://www.youtube.com/watch?v=8sjFA-IX-Ww

'''
class Queue():
    def __init__(self):
        self.size = 5
        self.queue = [None]* self.size
        #self.size = int(input("please enter the size of the queue"))
        self.front = 0;
        self.rear = -1;
        self.count = 0;

    def isEmpty(self):
        if self.count == 0: return True
        else: return False

    def isfull(self):
        if self.count == self.size: return True
        else: return False

    def enqueue(self,data):
        val = self.isfull()
        if not(val):
            self.rear = (self.rear + 1) % self.size
            #print(self.rear)
            self.queue[self.rear] = data
            self.count+=1
        else:
            print("Queue is Full")

    def dequeue(self):
        if not(self.isEmpty()):
            print("Element deleted is {}".format(self.queue[self.front]))
            self.front = (self.front + 1) % self.size
            self.count-=1
        else:
            print("Queue is empty")

    def display(self):
        print(self.queue)
        print("**start of the queue**", end = (" : "))

        if self.rear < self.front:
            for i in range(self.front, self.size):
                print(self.queue[i] , end = " <-- ")
            for i in range(0, self.rear+1):
                print(self.queue[i] , end = " <-- ")

        else:
            for i in range(self.front, self.rear+1):
                print(self.queue[i] , end = " <-- ")


q = Queue()
print(q.isEmpty())
q.enqueue(5)
q.enqueue(10)
q.dequeue()
q.enqueue(15)
q.enqueue(90)
q.enqueue(100)
#print(q.isfull())
q.enqueue(20)
print(q.isfull())
q.display()
