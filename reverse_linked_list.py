class Node:
    def __init__(self,data):
        self.data=data
        self.next= None

node1=Node(1)
node1.next =Node(2)
node1.next.next=Node(3)
node1.next.next.next=Node(4)

current=node1
list=[]
while(current!=None):
    list.append(int(current.data))
    current= current.next

list.reverse()
print(list)