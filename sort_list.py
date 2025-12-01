class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Print the linked list
def print_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# Merge two sorted lists
def merge(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.data < l2.data:
        l1.next = merge(l1.next, l2)
        return l1
    else:
        l2.next = merge(l1, l2.next)
        return l2

# Find the middle of the list
def get_middle(head):
    if head is None:
        return head

    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Merge sort for linked list
def merge_sort(head):
    if not head or not head.next:
        return head

    mid = get_middle(head)
    right_head = mid.next
    mid.next = None   # Split the list

    left = merge_sort(head)
    right = merge_sort(right_head)

    return merge(left, right)

# Insert at beginning
def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

# Example Usage
if __name__ == "__main__":
    head = None
    for value in [5, 3, 8, 1, 4]:
        head = push(head, value)

    print("Original list:")
    print_list(head)

    head = merge_sort(head)

    print("Sorted list:")
    print_list(head)
