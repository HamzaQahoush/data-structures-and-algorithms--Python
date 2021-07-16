class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def ll_append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __str__(self):
        values = list()

        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return f'{values}'
