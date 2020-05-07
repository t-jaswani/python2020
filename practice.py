class Node:
    def __init__(self,data,Nextnode = None):
        self.date = data
        self.Nextnode = Nextnode

    def getNextNode(self):
       return self.Nextnode


class Linklist:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def addNode(self,data):
        NewNode = Node(data,self.head)    
        self.head = NewNode
        self.size+=1

    def printNode(self):
       curr = self.head
       
       while curr:
           print(curr.date)
           #print(curr.getNextNode())
           curr = curr.getNextNode()
           
myList = Linklist()
print("Inserting")
myList.addNode(5)
myList.addNode(15)
myList.addNode(25)
print(myList.printNode())

"""
1 = (head= data=5, Nextnode=None)

2 = (head = data=15, Nextnode= 1)

3 = (head = data=25, NextNode =2)"""