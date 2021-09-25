"""
This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty
second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example,
in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32
(not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a
file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
"""


# I am assuming that the number of t's in /n/t/t/t.../t/ stands for the level in the tree
# Furthermore, I am assuming the format of the string to be consistent
# last but not least I'll make the assumption that this is actually a tree, i.e., it has no cycles


def trace_back(string_tree):
    return longest_path_to_file(deserialize(string_tree))


class FileTree:
    def __init__(self, val, children):
        self.val = val
        self.children = children


def longest_path_to_file(file_tree, max_path_length = 0):
    deepest_layer = True
    for child in file_tree.children:
        if child.children:
            deepest_layer = False
    if deepest_layer:
        for child in file_tree.children:
            print("Couldn't finish this in time")



# top level idea: deserialize the tree and then perform the operation on it
def deserialize(string_file_tree):
    # split off the root
    root = ''
    children = []
    i = 0
    while i < len(string_file_tree):
        if string_file_tree[i] == '\\':
            break
        else:
            root = root + string_file_tree[i]
            del string_file_tree[i]
            i += 1
    if not string_file_tree:
        return FileTree(root, [])
    else:
        # cut off first \n\t\tsomefile
        del string_file_tree[0:4]
        for subtree in find_subtree(string_file_tree):
            children.append(deserialize(subtree))


def find_subtree(string_file_tree):
    subtree = ''
    del string_file_tree[0:4]
    j = 0
    while j < len(string_file_tree):
        # cut of the next subtree beginning with \n\tsomefilename, do recursion afterwards
        if string_file_tree[j:j + 4] == "\\n\\t":
            if not string_file_tree[j + 5] == "\\":
                break
            else:
                # delete the \t\
                del string_file_tree[j+3:j+4]
                j += 1
        else:
            subtree += string_file_tree[j]
            del string_file_tree[j]
            j += 1
    if not string_file_tree:
        return [subtree]
    else:
        return [subtree] + find_subtree(string_file_tree)


if __name__ == '__main__':
    print()
