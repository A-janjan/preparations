class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None
        
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def apeend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node
        
    def delete_node(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            return
        prev = None
        current = self.head
        while current.next != self.head and current.data != data :
            prev = current
            current = current.next
        if current.data == data:
            prev.next = current.next
            current = None
            
    def print_list(self):
        current = self.head
        while True:
            print(current.data, end=" ")
            if current.next == self.head:
                break
            current = current.next
        print()