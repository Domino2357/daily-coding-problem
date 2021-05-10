"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


# Although this is strictly speaking one pass its still O(n*k) complexity. Right now, I can't come up with something smarter
def two_elements_add_up_to_k(input_list, k):
    # I assume that the list contains only positive integers.
    list_of_possible_subsums = []
    for number in input_list:
        if (k - number) in list_of_possible_subsums:
            return True
        if number not in list_of_possible_subsums:
            list_of_possible_subsums.append(number)
    return False


if __name__ == '__main__':
    print(two_elements_add_up_to_k([10, 15, 3, 7], 17))
