"""
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields,
it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list;
it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and
dereference_pointer functions that converts between nodes and memory addresses.
"""


# data: whats stored at the respective element, adr: address of the data,
# xor_next_prev: xor of the addresses of the previous and next nodes
class Node:
    def __init__(self, data, adr, xor_next_prev=None):
        self.data = data
        self.adr = adr
        self.xorNextPrev = xor_next_prev


class XORLinkedList:
    def __init__(self):
        self.current = None
        self.first = None

    def add_element(self, data):
        # no node has been assigned yet - this is the starting node
        if self.current is None:
            self.current = Node(data, get_pointer(data), get_pointer(data))
            self.first = Node(data, get_pointer(data), get_pointer(data))
        else:
            adr = get_pointer(data)
            # second element into the list
            if self.first.adr == self.current.adr:
                self.first.xorNextPrev = adr
                self.current = Node(data, adr, self.first.adr)
            # third, fourth, fifth, sixth, ... element
            else:
                curr_adr = self.current.adr
                self.current.xorNextPrev = self.current.xorNextPrev ^ adr
                self.current = Node(data, get_pointer(data), curr_adr)

    def find_by_index(self, index):
        next_node = dereference_pointer(self.first.xorNextPrev)
        prev_adr = dereference_pointer(self.first.adr)
        for i in range(1, index):
            used_prev_adr = prev_adr
            prev_adr = next_node.adr
            next_node = dereference_pointer(used_prev_adr ^ next_node.adr)
        return next_node


# dummy function because python has no pointer
def get_pointer(data):
    return 0


# dummy function because python has no pointer
def dereference_pointer(pointer):
    return Node(0, 0, 0)
