# Node class to simulate each node in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Data of the node
        self.next = None  # Pointer to the next node

# Function to display the addresses (memory locations) of the nodes
def display_node_addresses(head):
    current = head
    while current:
        # Using id() function to display memory address (pointer simulation)
        print(f"Node with data {current.data} is located at address {id(current)}")
        current = current.next

# Creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Linking nodes
node1.next = node2
node2.next = node3

# Displaying the addresses of nodes
display_node_addresses(node1)
display_node_addresses(node1)
