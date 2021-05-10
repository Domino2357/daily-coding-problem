"""
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""


# binary tree
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# find unival tree
def unival_tree(input_tree):
    count = 0
    if not (input_tree.left is None):
        count += unival_tree(input_tree.left)
    if not (input_tree.right is None):
        count += unival_tree(input_tree.right)
    if not (input_tree.left is None and input_tree.right is None):
        if input_tree.left.val == input_tree.right.val:
            count += 1
    if input_tree.left is None and input_tree.right is None:
        count += 1
    return count


if __name__ == '__main__':
    tree = (Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0))))
    print(unival_tree(tree))
