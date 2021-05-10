"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    if node.left is None and node.right is None:
        return str(node.val)
    elif node.left is None and node.right is not None:
        return str(node.val) + ' (' + serialize(node.right) + ')'
    elif node.left is not None and node.right is None:
        return str(node.val) + ' (' + serialize(node.left) + ')'
    else:
        return str(node.val) + ' (' + serialize(node.left) + ')' + '(' + serialize(node.right) + ')'


# did not find the solution in time, problem is, one can't even use regular expressions here because (..(())..) is no
# regular language
def deserialize(string_tree):
    # take the edge case where there is only a root and return a tree with this. Split at )(, strip away ( and ) at the
    # beginning of the left and right tree, recursively build the tree from there onwards.
    split_string = string_tree.split(' ', 1)
    root = split_string[0]
    if len(split_string) == 1:
        return Node(root)
    elif len(split_string) == 2:
        left_right_subtree = split_string[1]
        i = 1
        closed_brackets_count = 1
        while closed_brackets_count > 0:
            if left_right_subtree[i] == '(':
                closed_brackets_count += 1
            elif left_right_subtree[i] == ')':
                closed_brackets_count += -1
            i += 1
        last_index = len(left_right_subtree) - 1
        return Node(root, deserialize(left_right_subtree[1:i - 1]),
                    deserialize((left_right_subtree[i+1:last_index])))


if __name__ == '__main__':
    tree = Node('root', Node('left', Node('left.right'), Node('left.left')), Node('right'))
    print(serialize(deserialize(serialize(tree))))
