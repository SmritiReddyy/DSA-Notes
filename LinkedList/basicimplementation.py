"""
Basic Linked List Implementation
This file contains the fundamental node and linked list classes
that will be used across all problem solutions.
"""

class Node:
    """Node class for Singly Linked List"""
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    """Basic Singly Linked List with essential operations"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """Check if list is empty - O(1)"""
        return self.head is None
    
    def get_size(self):
        """Return the size of the list - O(1)"""
        return self.size
    
    def insert_at_beginning(self, data):
        """Insert node at the beginning - O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_at_end(self, data):
        """Insert node at the end - O(n)"""
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.size += 1
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
        self.size += 1
    
    def insert_at_position(self, data, position):
        """Insert node at specific position - O(n)"""
        if position < 0 or position > self.size:
            raise IndexError("Position out of bounds")
        
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        current = self.head
        
        for _ in range(position - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete_at_beginning(self):
        """Delete node at beginning - O(1)"""
        if self.is_empty():
            raise Exception("List is empty")
        
        deleted_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return deleted_data
    
    def delete_at_end(self):
        """Delete node at end - O(n)"""
        if self.is_empty():
            raise Exception("List is empty")
        
        if self.head.next is None:
            deleted_data = self.head.data
            self.head = None
            self.size -= 1
            return deleted_data
        
        current = self.head
        while current.next.next:
            current = current.next
        
        deleted_data = current.next.data
        current.next = None
        self.size -= 1
        return deleted_data
    
    def search(self, data):
        """Search for a value - O(n)
        Returns position if found, -1 otherwise"""
        current = self.head
        position = 0
        
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        
        return -1
    
    def display(self):
        """Display the linked list"""
        if self.is_empty():
            print("List is empty")
            return
        
        current = self.head
        elements = []
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" -> ".join(elements))
    
    def to_list(self):
        """Convert linked list to Python list for easier testing"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


# Helper function to create linked list from array
def create_linked_list(arr):
    """Create a linked list from an array"""
    if not arr:
        return LinkedList()
    
    ll = LinkedList()
    for item in arr:
        ll.insert_at_end(item)
    return ll


# Example usage
if __name__ == "__main__":
    print("=== Basic Linked List Operations ===\n")
    
    # Create a linked list
    ll = LinkedList()
    
    # Insert operations
    print("Inserting elements: 10, 20, 30, 40")
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    ll.display()
    
    print(f"\nSize: {ll.get_size()}")
    
    # Insert at beginning
    print("\nInserting 5 at beginning")
    ll.insert_at_beginning(5)
    ll.display()
    
    # Insert at position
    print("\nInserting 25 at position 3")
    ll.insert_at_position(25, 3)
    ll.display()
    
    # Search
    print("\nSearching for 30:")
    position = ll.search(30)
    print(f"Found at position: {position}")
    
    # Delete operations
    print("\nDeleting from beginning:")
    deleted = ll.delete_at_beginning()
    print(f"Deleted: {deleted}")
    ll.display()
    
    print("\nDeleting from end:")
    deleted = ll.delete_at_end()
    print(f"Deleted: {deleted}")
    ll.display()