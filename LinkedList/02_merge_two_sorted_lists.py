"""
Problem: Merge Two Sorted Linked Lists
File: LinkedList/04_merge_two_sorted_lists.py

Problem Statement:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by 
splicing together the nodes of the first two lists.

Example:
Input: list1 = 1 -> 2 -> 4, list2 = 1 -> 3 -> 4
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

Difficulty: Easy
Time Complexity: O(n + m) where n and m are lengths of the two lists
Space Complexity: O(1) iterative, O(n + m) recursive

LeetCode: #21 - Merge Two Sorted Lists
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_two_lists_iterative(head1, head2):
    """
    Merge two sorted lists iteratively using dummy node
    
    Algorithm:
    1. Create a dummy node to simplify edge cases
    2. Compare nodes from both lists
    3. Attach smaller node to result
    4. Move pointers forward
    
    Time: O(n + m), Space: O(1)
    """
    # Create dummy node
    dummy = Node(0)
    current = dummy
    
    # Traverse both lists
    while head1 and head2:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        
        current = current.next
    
    # Attach remaining nodes
    if head1:
        current.next = head1
    if head2:
        current.next = head2
    
    return dummy.next


def merge_two_lists_recursive(head1, head2):
    """
    Merge two sorted lists recursively
    
    Algorithm:
    1. Base case: if one list is empty, return the other
    2. Compare first nodes
    3. Recursively merge the rest
    
    Time: O(n + m), Space: O(n + m) due to recursion stack
    """
    # Base cases
    if not head1:
        return head2
    if not head2:
        return head1
    
    # Recursive case
    if head1.data <= head2.data:
        head1.next = merge_two_lists_recursive(head1.next, head2)
        return head1
    else:
        head2.next = merge_two_lists_recursive(head1, head2.next)
        return head2


def merge_two_lists_inplace(head1, head2):
    """
    Merge lists in-place without dummy node
    
    Time: O(n + m), Space: O(1)
    """
    if not head1:
        return head2
    if not head2:
        return head1
    
    # Determine which list starts first
    if head1.data <= head2.data:
        result = head1
        head1 = head1.next
    else:
        result = head2
        head2 = head2.next
    
    current = result
    
    # Merge remaining nodes
    while head1 and head2:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        
        current = current.next
    
    # Attach remaining nodes
    current.next = head1 if head1 else head2
    
    return result


def merge_k_sorted_lists(lists):
    """
    Merge K sorted linked lists
    
    Algorithm: Divide and conquer approach
    1. Pair up lists and merge them
    2. Repeat until only one list remains
    
    Time: O(N log k) where N is total nodes, k is number of lists
    Space: O(1) if not counting recursion
    """
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]
    
    # Merge lists pairwise
    while len(lists) > 1:
        merged_lists = []
        
        for i in range(0, len(lists), 2):
            list1 = lists[i]
            list2 = lists[i + 1] if i + 1 < len(lists) else None
            
            merged = merge_two_lists_iterative(list1, list2)
            merged_lists.append(merged)
        
        lists = merged_lists
    
    return lists[0]


def merge_sorted_array_to_list(head, arr):
    """
    Merge a sorted linked list with a sorted array
    Returns new linked list
    
    Time: O(n + m), Space: O(m) for new nodes from array
    """
    # Convert array to linked list first
    if not arr:
        return head
    
    arr_head = Node(arr[0])
    current = arr_head
    
    for i in range(1, len(arr)):
        current.next = Node(arr[i])
        current = current.next
    
    # Merge the two lists
    return merge_two_lists_iterative(head, arr_head)


# Helper functions
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
    """Convert linked list to array"""
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    return result


# Test cases
if __name__ == "__main__":
    print("=== Merge Two Sorted Linked Lists ===\n")
    
    # Test case 1: Normal merge
    print("Test 1: Merge two sorted lists")
    list1 = create_list([1, 2, 4])
    list2 = create_list([1, 3, 4])
    print("List 1: ", end="")
    print_list(list1)
    print("List 2: ", end="")
    print_list(list2)
    
    merged1 = merge_two_lists_iterative(list1, list2)
    print("Merged (iterative): ", end="")
    print_list(merged1)
    print()
    
    # Test case 2: One empty list
    print("Test 2: One empty list")
    list3 = create_list([1, 2, 3])
    list4 = None
    print("List 1: ", end="")
    print_list(list3)
    print("List 2: Empty")
    
    merged2 = merge_two_lists_iterative(list3, list4)
    print("Merged: ", end="")
    print_list(merged2)
    print()
    
    # Test case 3: Different lengths
    print("Test 3: Different lengths")
    list5 = create_list([1, 3, 5, 7, 9])
    list6 = create_list([2, 4])
    print("List 1: ", end="")
    print_list(list5)
    print("List 2: ", end="")
    print_list(list6)
    
    merged3 = merge_two_lists_recursive(list5, list6)
    print("Merged (recursive): ", end="")
    print_list(merged3)
    print()
    
    # Test case 4: Merge K sorted lists
    print("Test 4: Merge K sorted lists")
    lists = [
        create_list([1, 4, 5]),
        create_list([1, 3, 4]),
        create_list([2, 6])
    ]
    print("List 1: ", end="")
    print_list(lists[0])
    print("List 2: ", end="")
    print_list(lists[1])
    print("List 3: ", end="")
    print_list(lists[2])
    
    merged_k = merge_k_sorted_lists(lists)
    print("Merged K lists: ", end="")
    print_list(merged_k)
    print()
    
    # Test case 5: Merge with array
    print("Test 5: Merge list with sorted array")
    list7 = create_list([1, 3, 5])
    arr = [2, 4, 6, 8]
    print("List: ", end="")
    print_list(list7)
    print(f"Array: {arr}")
    
    merged_arr = merge_sorted_array_to_list(list7, arr)
    print("Merged: ", end="")
    print_list(merged_arr)