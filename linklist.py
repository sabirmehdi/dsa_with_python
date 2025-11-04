# Node class (like struct Node in C++)
class Node:
    def __init__(self, data):
        self.data = data       # stores data
        self.next = None       # pointer to next node


# LinkedList class (like class LinkedList in C++)
class LinkedList:
    def __init__(self):
        self.head = None       # initially empty list

    # function to insert a new node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    # function to display the list
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # function to insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # function to delete a node by value
    def delete_node(self, key):
        temp = self.head

        # if head node itself holds the key
        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # search for the key to be deleted
        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found!")
            return

        prev.next = temp.next
        temp = None


# ---- Testing the LinkedList ----
list1 = LinkedList()
n=1
num=input("Add node: ")
while(n!=0):
    
    list1.insert_at_end(num)
    list1.display()

    num=input("Add node: ")
    print("Exit")
    n=int(input())
   
#list1.insert_at_beginning(5)
#list1.display()          # Output: 5 -> 10 -> 20 -> 30 -> None

#list1.delete_node(20)
#list1.display()          # Output: 5 -> 10 -> 30 -> None
