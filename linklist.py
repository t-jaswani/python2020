""" 
Attributes of a linked List
1) There are two types of LL single and double ended 
2) A Single ended link list will have data and informtion about the next entry a->b->c->d
3) Double sided liked list will have data, info on the next and previous entry a<->b<->c<->d
4)  A single entry in a linked list is called a node """

# A class is a representaion of real world object 

class Queue:
    def __init__(self):
        self.q = list()

    #Functionality to add to the queue

    def add(self, data):
        if data not in self.q:
            self.q.insert(0,data)
            return True
        return False
    
    #Functionality to removing from a queue 
    def remove(self, data):
        if len(self.q) > 0:
            return self.q.pop()
        return "The queue is empty" 

class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.next = None

class LinkedList:
    def __init__(self):
        self.headval = None

    def get_values(self,Node):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.next

thelist = LinkedList()
thelist.headval = Node("a")
v2= Node("b")
v3=Node("c")
v4=Node("d")


thelist.get_values()        

