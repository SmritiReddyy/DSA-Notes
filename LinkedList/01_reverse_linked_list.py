"""
Problem: Reverse a Linked List

Problem Statement:
Given the head of a singly linked list, reverse the list and return the reversed list.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 5 -> 4 -> 3 -> 2 -> 1

Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_iterative(head):
    """
    Reverse linked list using iterative approach
    
    Algorithm:
    1. Use three pointers: prev, current, next
    2. Iterate through the list
    3. Reverse the link for each node
    4. Move pointers forward
    
    Time: O(n), Space: O(1)
    """
    prev = None
    current = head
    
    while current:
        # Store next node
        next_node = current.next
        
        # Reverse the link
        current.next = prev
        
        # Move pointers forward
        prev = current
        current = next_node
    
    # prev is now the new head
    return prev


def reverse_recursive(head):
    """
    Reverse linked list using recursive approach
    
    Algorithm:
    1. Base case: if head is None or only one node, return head
    2. Recursively reverse the rest of the list
    3. Fix the links
    
    Time: O(n), Space: O(n) due to recursion stack
    """
    # Base case
    if head is None or head.next is None:
        return head
    
    # Reverse the rest of the list
    new_head = reverse_recursive(head.next)
    
    # Fix the links
    head.next.next = head
    head.next = None
    
    return new_head


# Helper functions for testing
def create_list(arr):
    """Create linked list from array"""
    if not arr:
        return None
    
    head = Node(arr[0])
    current = head
    
    for i in range(1, len(arr)):
        current.next = Node(arr[i])
        current = current.next
    
    return head


def print_list(head):
    """Print linked list"""
    if not head:
        print("Empty list")
        return
    
    current = head
    elements = []
    
    while current:
        elements.append(str(current.data))
        current = current.next
    
    print(" -> ".join(elements))


def list_to_array(head):
    """Convert linked list to array for testing"""
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    return result


# Test cases
if __name__ == "__main__":
    print("=== Reverse Linked List ===\n")
    
    # Test case 1: Normal list
    print("Test 1: Normal list")
    head1 = create_list([1, 2, 3, 4, 5])
    print("Original: ", end="")
    print_list(head1)
    
    reversed1 = reverse_iterative(head1)
    print("Reversed: ", end="")
    print_list(reversed1)
    print()
    
    # Test case 2: Two elements
    print("Test 2: Two elements")
    head2 = create_list([1, 2])
    print("Original: ", end="")
    print_list(head2)
    
    reversed2 = reverse_recursive(head2)
    print("Reversed: ", end="")
    print_list(reversed2)
    print()
    
    # Test case 3: Single element
    print("Test 3: Single element")
    head3 = create_list([1])
    print("Original: ", end="")
    print_list(head3)
    
    reversed3 = reverse_iterative(head3)
    print("Reversed: ", end="")
    print_list(reversed3)
    print()
    
    # Test case 4: Empty list
    print("Test 4: Empty list")
    head4 = None
    print("Original: ", end="")
    print_list(head4)
    
    reversed4 = reverse_iterative(head4)
    print("Reversed: ", end="")
    print_list(reversed4)