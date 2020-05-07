class Node:

    def __init__(self,data,nextNode=None,prevNode=None):
       self.data = data # Store the value of the node
       self.nextNode = nextNode  # store the memory slot of the previous node
       self.prevNode = prevNode # store the memory slot of the next node
 

    def getData(self):
       return self.data

    def setData(self,val):
       self.data = val

    def getNextNode(self):
       return self.nextNode

    def prevNode(self):
       return self.prevnode    

    def setNextNode(self,val):
       self.nextNode = val

class LinkedList:

    def __init__(self,head = None, tail = None):
       self.head = head # Store memory location of the previous node
       self.tail = tail# store memory location of the latests node
       self.size = 0

    def getSize(self):
       return self.size

    def addNode(self,data):
       newNode = Node(data,self.head, self.tail)
       self.head = newNode  # (data, nextnode, prevNode)
       self.tail = self.head
       self.size+=1
       return True
       
    def printNextNodes(self):
       curr = self.head
       
       while curr:
           print(curr.data)
           curr = curr.getNextNode()
    
    def printPrevNodes(self):
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.prevNode()

myList = LinkedList()
myList.addNode("A")
myList.addNode("B")

myList.printPrevNodes()



"""
a<-->b



a-->b-->c<-->d
prevnode = tail
the memory location of c(latest node) needs to be inserted in d(last node)
"""

