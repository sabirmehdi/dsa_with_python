# Node class to store data and pointer to next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class to handle nodes
class LinkedList:
    def __init__(self):
        self.head = None

    # Function to add nodes at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Function to delete a node by its position
    def delete_middle(self):
        if self.head is None or self.head.next is None:
            print("No middle node to delete")
            return

        # Since we have 3 nodes, middle node is the second
        second_node = self.head.next
        self.head.next = second_node.next
        second_node = None  # optional, helps with memory

    # Function to print linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# ----------------------
# Main code
# ----------------------
ll = LinkedList()

# Create 3 nodes using a loop
for i in range(1, 4):
    ll.append(i)

print("Original linked list:")
ll.print_list()

# Delete middle node
ll.delete_middle()

print("Linked list after deleting middle node:")
ll.print_list()
