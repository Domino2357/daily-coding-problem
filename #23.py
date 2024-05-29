"""
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall.
 Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the
end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right.
 You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is
7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
"""
# assuming no complexity bounds
# first thoughts: we do not need a dijkstra for this problem. essentially all we need to do is to check at each level
# second thought: the wall can also be vertical so first thoughts are invalid


def find_min_steps(matrix, start, end):
    if start == end:
        return 0
    row_number = start[0]-end[0]
    start_neighbors = []
    if row_number > 0 and start[0] < len(matrix)-1:
        start_neighbors.append(matrix[start[0]+1][start[1]])
    elif row_number < 0 and start[0] > 0:
        start_neighbors.append(matrix[start[0]-1][start[1]])
    if start[1] < len(matrix[0])-1:
        start_neighbors.append(matrix[start[0]][start[1]+1])
    if start[1] > 0:
        start_neighbors.append(matrix[start[0][start[1]-1]])



