"""
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

"""

"""
First thoughts: this looks easy. I could window through the array, but this would give me O(n*k) time. So thats the catch here.
I think one has to delete all the numbers in intervall k except the max and then move one step further- this way only two numbers
ought to be compared each time, thus, making it possible to do it in O(n*2) = O(n) time constricted. The edge case that the max
is the first number to be handled needs to be considered.
"""


def print_max_numbers(array, interval_size):
    cur_max = (0, 0)
    max_afterward = (0, 0)
    # initialize with the first intervall, also cover case len(array) == intervall_size
    for i in range(0, interval_size):
        if array[i] >= cur_max[0]:
            cur_max = (array[i], i)
            max_afterward = (0, 0)
        if array[j] >= max_afterward[0] and array[i] < cur_max[0]:
            max_afterward = (array[i], i)
        del array[i]
    print(cur_max)
    for j in range(0, len(array)):
        if cur_max[1] == 0:
            cur_max = max_afterward
            max_afterward = (0, 0)
        else:
            cur_max[1] += -1
        if array[j] >= cur_max:
            cur_max = (array[j], interval_size-1)
            max_afterward = (0, 0)





