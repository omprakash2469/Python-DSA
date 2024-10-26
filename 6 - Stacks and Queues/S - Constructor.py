class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        current = self.top
        while current:
            print(current.value)
            current = current.next


new_stack = Stack(1)
new_stack.print_stack()