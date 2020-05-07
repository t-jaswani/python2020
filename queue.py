'''
FIFO policy
you can only add from the end 
you can only remove from the front of the queue
'''
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

"""
Read up and implement linked list 

what is a node?
Types of linked lists - singly linked lists and double linked list
[9,4,5,3]
singly linked list = a->b->c->d
double linked list = a<->b<->c<->d

- What is traversal. implement it in a sample code

500- 24/7


- linked lists (A good implementation/example of a queue) == Queue 

"""

class Node:

   def __init__(self,data,nextNode=None):
       self.data = data
       self.nextNode = nextNode
 

   def getData(self):
       return self.data

   def setData(self,val):
       self.data = val

   def getNextNode(self):
       return self.nextNode

   def setNextNode(self,val):
       self.nextNode = val

class LinkedList:

   def __init__(self,head = None):
       self.head = head
       self.size = 0

   def getSize(self):
       return self.size

   def addNode(self,data):
       newNode = Node(data,self.head)
       self.head = newNode # memory location of the node is passed to self.head
       self.size+=1
       #return True
       
   def printNode(self):
       curr = self.head
       
       while curr:
           print(curr.data)
           curr = curr.getNextNode()

myList = LinkedList()
print("Inserting")
print(myList.addNode(5))
print(myList.addNode(15))
print(myList.addNode(25))
print("Printing")
myList.printNode()
print("Size")
print(myList.getSize())

"""
--------------
def __new__(self):
- Create a double linked list with 10 items 
Use classes """