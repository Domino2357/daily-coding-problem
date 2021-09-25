import math

"""
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
"""

"""
Hopefully, there are no complexity constraints, otherwise, this would become very ugly.
I'll assume that the matrix looks like this (minus syntax for better readability:
matrix = [ [1, [4,  [7,
            2,  5,   8,
            3], 6]   9] ]
"""

result_list = []


def find_shortest_path(h_c_matrix):
    transverse_matrix(0, 0, h_c_matrix)
    return min(result_list)


def transverse_matrix(start, i, h_c_matrix):
    for entry in h_c_matrix[i]:
        follows = start + entry
        if i != len(h_c_matrix)-1:
            transverse_matrix(follows, i+1, h_c_matrix)
        else:
            result_list.append(follows)

