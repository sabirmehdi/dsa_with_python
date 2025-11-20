class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_nodes_and_addresses(self):
        temp = self.head
        while temp:
            print(f"Node data: {temp.data}, Address: {hex(id(temp))}")
            temp = temp.next

# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

ll.print_nodes_and_addresses()
