class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def remove_duplicates(self):
        current = self.head
        while current and current.next:
            if current.value == current.next.value:
                current.next = current.next.next
            else:
                current = current.next

# Usage
linked_list = SinglyLinkedList()
linked_list.append(1)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(3)
linked_list.append(4)

print("Original sorted linked list with duplicates:")
linked_list.print_list()

linked_list.remove_duplicates()

print("Linked list after removing duplicates:")
linked_list.print_list()
