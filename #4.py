"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words,
 find the lowest positive integer that does not exist in the array. The array can contain duplicates and
 negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


# i really had no clue how to do it in linear time and constant space, here are some answers, though:
# https://stackoverflow.com/questions/51346136/given-an-array-of-integers-find-the-first-missing-positive-integer-in-linear-ti
# using the indices does the trick


def lowest_integer(numbers):
    min_number = min(numbers)
    max_number = max(numbers)
    if (min_number > 1):
        return 1
    else:
        lowest_integer = max_number + 1


"""
kudos to pmcarpan from stackoverflow:

Assuming the array can be modified,

We divide the array into 2 parts such that the first part consists of only positive numbers. Say we have the starting index as 0 and the ending index as end(exclusive).

We traverse the array from index 0 to end. We take the absolute value of the element at that index - say the value is x.

If x > end we do nothing.
If not, we make the sign of the element at index x-1 negative. (Clarification: We do not toggle the sign. If the value is positive, it becomes negative. If it is negative, it remains negative. In pseudo code, this would be something like if (arr[x-1] > 0) arr[x-1] = -arr[x-1] and not arr[x-1] = -arr[x-1].)
Finally, we traverse the array once more from index 0 to end. In case we encounter a positive element at some index, we output index + 1. This is the answer. However, if we do not encounter any positive element, it means that integers 1 to end occur in the array. We output end + 1.

It can also be the case that all the numbers are non-positive making end = 0. The output end + 1 = 1 remains correct.

All the steps can be done in O(n) time and using O(1) space.

Example:

Initial Array:            1 -1 -5 -3 3 4 2 8
Step 1 partition:         1 8 2 4 3 | -3 -5 -1, end = 5
In step 2 we change the signs of the positive numbers to keep track of which integers have already occurred. For example, here array[2] = -2 < 0, it suggests that 2 + 1 = 3 has already occurred in the array. Basically, we change the value of the element having index i to negative if i+1 is in the array.

Step 2 Array changes to: -1 -8 -2 -4 3 | -3 -5 -1
In step 3, if some value array[index] is positive, it means that we did not find any integer of value index + 1 in step 2.

Step 3: Traversing from index 0 to end, we find array[4] = 3 > 0
        The answer is 4 + 1 = 5
        
"""
