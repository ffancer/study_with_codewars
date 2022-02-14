class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def get_nth(node, index):
    pass


def v():
    # list = build_one_two_three()
    print(get_nth(list, 0).data, 1, "First node should be located at index 0.")
    print(get_nth(list, 1).data, 2, "Second node should be located at index 1.")
    print(get_nth(list, 2).data, 3, "Third node should be located at index 2.")
    print("Invalid index value should throw error.", lambda: get_nth(list, 3))
    print("Invalid index value should throw error.", lambda: get_nth(list, -1))
    print("Invalid index value should throw error.", lambda: get_nth(list, 100))
    print("None linked list should throw error.", lambda: get_nth(None, 0))


print(v())