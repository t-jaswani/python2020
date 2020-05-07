class Node:

   def __init__(self,data,nextNode=None,prevNode=None):
       self.data = data
       self.nextNode = nextNode
       self.prevNode = prevNode
 

   def getData(self):
       return self.data

   def setData(self,val):
       self.data = val

   def getNextNode(self):
       return self.nextNode

   def getPrevNode(self):
       return self.prevNode    

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
       self.head = newNode
       print("Data-->",self.head.data)
       self.size+=1
       return True
       
   def printNodeFront(self):
       curr = self.head
       while curr:
           print(curr.data)
           curr = curr.getNextNode()

   def printNodeBack(self):
       curr = self.head
       while curr:
           print(curr.data)
           curr = curr.getPrevNode()        

myList = LinkedList()
print("Inserting")
print(myList.addNode(5))
print(myList.addNode(15))
print(myList.addNode(25))
print("Printing")
myList.printNode()
print("Size")
print(myList.getSize())
