"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

"""


def sum_consecutive(input_list):
    if len(input_list) == 0:
        print("Received empty list")
        return 0
    else:
        new_max = input_list[0]
        old_max = input_list[0]
    last_element_changed = 0
    for i in range(1, len(input_list)):
        maybe_new_max = input_list[i] + old_max
        if maybe_new_max > new_max:
            old_max = new_max
            new_max = maybe_new_max
            last_element_changed = i
        # if the current number does not lead to a new max, we skip it, it also adds no value to the max,
        # therefore, we increase it
        elif last_element_changed == i - 1:
            old_max = new_max
            pass
        # if one element is skipped we can safely add this new one
        else:
            old_max = new_max
            new_max = new_max + input_list[i]
            last_element_changed = i
    return new_max


if __name__ == '__main__':
    print(sum_consecutive([1, 9, 13, 17, 16, 3, 9, 8, 16, 16]))
