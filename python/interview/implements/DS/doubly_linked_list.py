class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None
        

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
            
    def delete_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                current = None
                return
            current = current.next
            
    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
        
        
    def print_backward(self):
        current = self.head
        while current and current.next:
            current = current.next
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()
        
        
        
# Example usage:
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(4)
    dll.delete_node(2)
    
    print("Forward:")
    dll.print_forward()  # Output: 4 1 3
    
    print("Backward:")
    dll.print_backward()  # Output: 3 1 4