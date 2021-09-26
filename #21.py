"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

# assuming no complexity restraints and that I can manipulate the list on the fly
# first thought: look for every pair in the list if there is an overlap. Save all the overlap and check if they overlap
# second thought: simply iterating without list comprehension leads to higher complexity,
# recursion is more elegant (at least in Python)


def additional_rooms(time_intervals):
    first_element = time_intervals.pop(0)
    overlaps = []
    time_intervals[:] = [overlaps.append(interval) if first_element[0] in range(interval[0], interval[1])
                         else interval for interval in time_intervals]
    if overlaps:
        # we need at least one additional room because of the overlap, plus, all the additional overlaps
        return 1 + additional_rooms(overlaps)
    if not time_intervals:
        # no rooms left
        return 0


def find_minimal_class_rooms(time_intervals):
    # one room is the basis
    return 1 + additional_rooms(time_intervals)


if __name__=='__main__':
    print(find_minimal_class_rooms([[30, 75], [0, 50], [60, 150], [140, 160]]))
