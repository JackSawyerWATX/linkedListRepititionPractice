# Linked List Implementation in Python
# A linked list is a linear data structure where elements are stored in nodes
# Each node contains data and a reference (link) to the next node in the sequence

class Node:
    """
    Node class represents a single element in the linked list
    Each node contains:
    - data: the actual value stored in the node
    - next: a reference/pointer to the next node in the list
    """
    
    def __init__(self, data):
        """
        Initialize a new node with the given data
        Set next to None initially (no connection to other nodes yet)
        """
        self.data = data  # Store the data value
        self.next = None  # Initialize next pointer to None


class LinkedList:
    """
    LinkedList class manages the entire linked list structure
    It keeps track of the head (first node) of the list
    """
    
    def __init__(self):
        """
        Initialize an empty linked list
        head points to the first node (None for empty list)
        """
        self.head = None  # Start with an empty list
    
    def append(self, data):
        """
        Add a new node with the given data at the end of the list
        Time Complexity: O(n) - we need to traverse to the end
        """
        new_node = Node(data)  # Create a new node with the given data
        
        # If the list is empty, make the new node the head
        if not self.head:
            self.head = new_node
            return
        
        # If list is not empty, traverse to the end
        current = self.head  # Start from the head
        while current.next:  # Keep going until we find a node with no next
            current = current.next  # Move to the next node
        
        # Now current is the last node, so link it to the new node
        current.next = new_node
    
    def prepend(self, data):
        """
        Add a new node with the given data at the beginning of the list
        Time Complexity: O(1) - constant time operation
        """
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.head  # Point new node to current head
        self.head = new_node  # Make new node the new head
    
    def delete(self, data):
        """
        Delete the first occurrence of a node with the given data
        Time Complexity: O(n) - might need to search entire list
        """
        # If list is empty, nothing to delete
        if not self.head:
            return
        
        # If the head node contains the data to delete
        if self.head.data == data:
            self.head = self.head.next  # Move head to next node
            return
        
        # Search for the node to delete
        current = self.head
        while current.next:  # While there's a next node to check
            if current.next.data == data:  # If next node has the data
                # Skip the next node by linking to the node after it
                current.next = current.next.next
                return
            current = current.next  # Move to next node
    
    def find(self, data):
        """
        Search for a node with the given data
        Returns True if found, False otherwise
        Time Complexity: O(n) - might need to search entire list
        """
        current = self.head  # Start from the head
        while current:  # While there are nodes to check
            if current.data == data:  # If we found the data
                return True
            current = current.next  # Move to next node
        return False  # Data not found
    
    def get_size(self):
        """
        Count and return the number of nodes in the list
        Time Complexity: O(n) - need to traverse entire list
        """
        count = 0
        current = self.head  # Start from the head
        while current:  # While there are nodes to count
            count += 1
            current = current.next  # Move to next node
        return count
    
    def display(self):
        """
        Print all elements in the list in order
        Time Complexity: O(n) - visit each node once
        """
        if not self.head:  # If list is empty
            print("List is empty")
            return
        
        elements = []  # Store elements for printing
        current = self.head  # Start from the head
        
        while current:  # While there are nodes to visit
            elements.append(str(current.data))  # Add data to our list
            current = current.next  # Move to next node
        
        # Print all elements connected with arrows to show the links
        print(" -> ".join(elements) + " -> None")
    
    def insert_at_position(self, position, data):
        """
        Insert a new node with given data at the specified position
        Position 0 means insert at the beginning
        Time Complexity: O(n) - might need to traverse to position
        """
        # If inserting at the beginning (position 0)
        if position == 0:
            self.prepend(data)
            return
        
        new_node = Node(data)  # Create new node
        current = self.head
        
        # Traverse to the position just before where we want to insert
        for i in range(position - 1):
            if current is None:  # If position is beyond list length
                print(f"Position {position} is out of bounds")
                return
            current = current.next
        
        # If we've gone beyond the list
        if current is None:
            print(f"Position {position} is out of bounds")
            return
        
        # Insert the new node
        new_node.next = current.next  # New node points to what current points to
        current.next = new_node  # Current now points to new node
    
    def reverse(self):
        """
        Reverse the entire linked list
        Time Complexity: O(n) - visit each node once
        """
        previous = None  # Keep track of previous node
        current = self.head  # Start with current node
        
        while current:  # While there are nodes to process
            next_node = current.next  # Store next node before we lose it
            current.next = previous  # Reverse the link
            previous = current  # Move previous forward
            current = next_node  # Move current forward
        
        self.head = previous  # Update head to point to new first node


# Example usage and demonstration
if __name__ == "__main__":
    """
    This section demonstrates how to use the LinkedList class
    It will only run when you execute this file directly
    """
    
    print("=== Linked List Demo ===\n")
    
    # Create a new empty linked list
    my_list = LinkedList()
    
    print("1. Creating an empty list:")
    my_list.display()
    
    print("\n2. Adding elements to the end of the list:")
    my_list.append(1)
    print("After adding 1:")
    my_list.display()
    
    my_list.append(2)
    print("After adding 2:")
    my_list.display()
    
    my_list.append(3)
    print("After adding 3:")
    my_list.display()
    
    print("\n3. Adding element to the beginning:")
    my_list.prepend(0)
    print("After prepending 0:")
    my_list.display()
    
    print(f"\n4. List size: {my_list.get_size()}")
    
    print("\n5. Searching for elements:")
    print(f"Is 2 in the list? {my_list.find(2)}")
    print(f"Is 5 in the list? {my_list.find(5)}")
    
    print("\n6. Inserting at specific position:")
    my_list.insert_at_position(2, 1.5)
    print("After inserting 1.5 at position 2:")
    my_list.display()
    
    print("\n7. Deleting an element:")
    my_list.delete(1.5)
    print("After deleting 1.5:")
    my_list.display()
    
    print("\n8. Reversing the list:")
    my_list.reverse()
    print("After reversing:")
    my_list.display()
    
    print("\n=== Demo Complete ===")
