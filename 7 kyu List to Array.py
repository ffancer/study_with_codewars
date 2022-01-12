class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def list_to_array(node):
    print(node.value)


u = LinkedList(1)
print(list_to_array(u), [1])

u = LinkedList(4, LinkedList(25, LinkedList(30)))
print(list_to_array(u), [4, 25, 30])

u = LinkedList(2, LinkedList(40, LinkedList(43, LinkedList(25, LinkedList(125)))))
print(list_to_array(u), [2, 40, 43, 25, 125])
