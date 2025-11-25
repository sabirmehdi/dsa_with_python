class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None
n1=Node(10)

n2=Node(20)  
n3=None

n1.next = n2           
n1.data = 1000

n2.next = n3
n3.next= n4
n4.next =  None
current_node = n1
while current_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.next
print("None")
