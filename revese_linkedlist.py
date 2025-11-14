class Node:
    """
    Every item in our list is a 'Node'.
    It holds a value and a pointer (link) to the next Node.
    """
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next_node = next_node


def reverse_list(head):
    """
    Flips the direction of the links in the list.
    We use three variables to keep track of where we are.
    """
    
    
    previous = None
    
    current = head
    
    while current is not None:
        
        next_to_process = current.next_node
        
        current.next_node = previous
        
        previous = current
        
        current = next_to_process
        
    return previous


def create_list(data):
    """Helper to build a list from a simple Python list."""
    if not data:
        return None
    head = Node(data[0])
    current = head
    for value in data[1:]:
        current.next_node = Node(value)
        current = current.next_node
    return head

def print_list(head):
    """Helper to print the list values."""
    values = []
    current = head
    while current:
        values.append(str(current.value))
        current = current.next_node
    print(" -> ".join(values))

if __name__ == "__main__":
    
    start_data = [1, 2, 3, 4]
    my_list = create_list(start_data)
    
    print("Original List:")
    print_list(my_list)
    
    # Reverse it!
    reversed_list = reverse_list(my_list)
    
    print("\nReversed List:")
    print_list(reversed_list)