class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False



 
my_linked_list = LinkedList(4)
my_linked_list.append(12)
my_linked_list.append(20)
my_linked_list.set(1, 100)

my_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    4
    100
    20

"""