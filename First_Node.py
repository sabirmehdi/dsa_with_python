class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1= Node(11)
node2=Node(22)

node1.next=node2
node2.next.=node3

print(node2.data) // 

current =node1

while(current!=None):
    print(current.data, end= " ")
    current=current.next
