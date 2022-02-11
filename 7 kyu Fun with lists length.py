# 7 kyu
# Fun with lists: length

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def length(head):
    cnt = 0

    while head:
        head = head.next
        cnt += 1

    return cnt




def example_test_case():
    head = None
    print(length(head), 0)

    n1 = Node(1)
    n2 = Node(2, n1)
    n3 = Node(3, n2)
    head = Node(4, n3)
    print(length(head), 4)

example_test_case()

