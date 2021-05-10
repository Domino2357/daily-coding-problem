"""
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function
that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive
integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""


# this is actually just the fibonacci number- if we increase step k by one, we can add 1's to each possibility at k,
# moreover we can add a 2 to all possibilities at step k-1: f(k+1) = f(k) + f(k-1)
def function_for_1_and_2(number_of_steps):
    if number_of_steps <= 0:
        return 0
    if number_of_steps == 1:
        return 1
    if number_of_steps == 2:
        return 2
    else:
        return function_for_1_and_2(number_of_steps - 1) + function_for_1_and_2(number_of_steps - 2)


# to generalize this we need to think about fibonacci numbers more abstractly. While for X = {1, 2} we had
# f(k+1) = f(k) + f(k-1), for arbitrary numbers  X = { n1, n2, ..., nn }  this would add up to f(k+1) =
# f(k-n1) + f(k-n2) ... + f(k-nn). We need to take into account every possible combination of steps with each other.
def function_for_arbitrary_step_lengths(number_of_steps, list_of_step_lengths):
    if number_of_steps <= 0:
        return 0
    sum_of_possibilities = 0
    for step_length in list_of_step_lengths:
        if number_of_steps > step_length:
            sum_of_possibilities += function_for_arbitrary_step_lengths(number_of_steps - step_length,
                                                                        list_of_step_lengths)
        elif number_of_steps == step_length:
            sum_of_possibilities += 1
        else:
            pass
    return sum_of_possibilities


if __name__ == '__main__':
    print(function_for_arbitrary_step_lengths(19, [2, 3, 5]))
