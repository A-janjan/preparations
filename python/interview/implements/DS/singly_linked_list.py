class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def prepend(self, data):
        new_data = Node(data)
        new_data.next = self.head
        self.head = new_data
        
    def delete_node(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current != data:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None
        
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            
            
# Example usage:
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.prepend(4)
    sll.delete_node(2)
    sll.print_list()