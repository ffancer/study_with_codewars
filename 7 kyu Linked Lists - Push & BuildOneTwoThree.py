class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):


    pass


def build_one_two_three():


    pass

print(push(None, 1).data, 1, "Should be able to create a new linked list with push().")
print(push(None, 1).next, None, "Should be able to create a new linked list with push().")
print(push(Node(1), 2).data, 2, "Should be able to prepend a node to an existing node.")
print(push(Node(1), 2).next.data, 1, "Should be able to prepend a node to an existing node.")

print(build_one_two_three().data, 1, "Value at index 0 should be 1.")
print(build_one_two_three().next.data, 2, "Value at index 1 should be 2.")
print(build_one_two_three().next.next.data, 3, "Value at index 2 should be 3.")
print(build_one_two_three().next.next.next, None, "Value at index 3 should be null.")
