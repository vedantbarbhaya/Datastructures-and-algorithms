class Node():
    def __init__(self,data,priority):
        self.data = data
        self.priority = priority

class PQueue():
    def __init__(self):
        self.size = 7
        self.queue = [None]* self.size
        #self.size = int(input("please enter the size of the queue"))
        self.count = 0;

    def isEmpty(self):
        if self.count == 0: return True
        else: return False

    def isfull(self):
        if self.count == self.size: return True
        else: return False

    def insert(self,ele):
        '''
        @params
        ele - a tuple of form (data,priority)
        '''
        node = Node(ele[0],ele[1])

        if self.count == 0:
            self.queue.append(node)
            self.queue.reverse()
            self.count+=1
        else:
            if not(self.isfull()):
                    self.count+=1
                    pos = 0
                    temp = 0
                    ins_flag = 0

                    # find the position to insert new node
                    for i in range(0,self.size):
                        if (self.queue[i]!= None and node.priority > self.queue[i].priority):
                            pos = i
                            ins_flag = 1
                            temp = self.queue[i]
                            self.queue[i] = node
                            break
                        elif (self.queue[i] == None):
                            self.queue[i] = node
                            break

                    # if an insertion operation took place, shift all the ele one place ahead
                    if ins_flag == 1:
                        for i in range(pos+1,self.size):
                           temp, self.queue[i] = self.queue[i] , temp

            else:
                print("Queue is full")

    def pop(self):
        if not(self.isEmpty()):
            print("element popped is: " + str(self.queue[0].data))
            self.queue.pop(0)
        else:
            print("Queue is empty")

    def display(self):
        for i in self.queue:
            if i != None:
                print(str(i.data) + "," + str(i.priority) , end = " | ")
        print()





'''
insert(ele,priority number)
'''
priorityq = PQueue()
priorityq.insert(("A",2))
priorityq.insert(("B",3))
priorityq.insert(("C",1))
priorityq.insert(("K",4))
priorityq.insert(("Z",6))
priorityq.insert(("D",0))
priorityq.insert(("L",20))
priorityq.display()
priorityq.pop()
priorityq.display()
