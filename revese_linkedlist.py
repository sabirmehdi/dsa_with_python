class ListNode:
    """Blueprint for a single node in the linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode | None) -> ListNode | None:
    """
    Reverses a singly linked list iteratively using three pointers.
    """
    
    # 'prev' tracks the node that has already been reversed (new end).
    prev = None
    current = head
    
    while current is not None:
        
        next_node = current.next
        
        # Reverse the pointer: current node points backward to 'prev'.
        current.next = prev
        
        prev = current
        current = next_node
        
    # 'prev' is the new head of the reversed list.
    return prev

def create_linked_list(data: list) -> ListNode | None:
    if not data:
        return None
    head = ListNode(data[0])
    current = head
    for val in data[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head: ListNode | None):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values))

if __name__ == "__main__":
    
    # Create the original list: 1 -> 2 -> 3 -> 4 -> None
    original_data = [1, 2, 3, 4]
    head = create_linked_list(original_data)
    
    print("Original List:")
    print_linked_list(head)
    
    # Call the reversal function
    reversed_head = reverse_list(head)
    
    print("\nReversed List:")
    print_linked_list(reversed_head)
    
    # Test a case with an empty list
    empty_list_head = create_linked_list([])
    reversed_empty_list = reverse_list(empty_list_head)
    print("\nReversed Empty List (should be nothing):")
    print_linked_list(reversed_empty_list)