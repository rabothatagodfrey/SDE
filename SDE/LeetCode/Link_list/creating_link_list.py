class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class link_list:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


if __name__ == "__main__":
    ll = link_list()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.print_list()