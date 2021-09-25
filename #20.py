"""
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""


# assuming, henceforth, that there is only one pointer to a next node, i.e., if A and B intersect, they are identical
# afterwards. Consequently, the "tail" must be equal

class LinkedList:
    def __init__(self, next_node=None, value = 0):
        self.next_node = next_node
        self.value = value

    def add_node(self, node):
        self.next_node = node

    def has_next(self):
        if self.next_node is None:
            return False
        else:
            return True

    def length(self):
        if self.next_node is None:
            return 1
        else:
            return 1 + self.next_node.length()

    def get_next(self):
        return self.next_node


def check_lists(A, B):
    length_difference = abs(A.length() - B.length())
    current_a = A
    current_b = B
    for i in range(0, length_difference):
        if A.length() > B.length():
            current_a = current_a.get_next()
        else:
            current_b = current_b.get_next()

    while current_a.has_next():
        if current_a == current_b:
            return current_a
        else:
            current_a = current_a.get_next()
            current_b = current_b.get_next()

    return None

if __name__=='__main__':
    f = LinkedList(None, 1)
    e = LinkedList(f, 2)
    d = LinkedList(e, 3)
    c = LinkedList(e, 4)
    b = LinkedList(d, 4)
    a = LinkedList(c, 5)

    print(check_lists(a, b).value)