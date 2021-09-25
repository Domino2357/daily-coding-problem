"""
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
"""

"""
This is a graph problem. First construct a graph out of all matrix elements: from the starting point, go to all possible
colors of house 1, with edge cost equal to the building cost. For each vertex build an edge to the vertices of house 2
except for the one with the same color. Continue until house N. Connect all of them to a destination vertex with
no edge cost. Then do a dijkstra.
I'll assume that the matrix looks like this (minus syntax for better readability:
matrix = [ [1, [4,  [7,
            2,  5,   8,
            3], 6]   9] ]
"""


def graph_constr(h_c_matrix):
    graph = {}
    graph.update({"start": []})
    node_index = 0
    # initialize
    color_index = 0
    for color in h_c_matrix[0]:
        graph["start"].append((node_index, color))
    # fill
    for row in h_c_matrix:

