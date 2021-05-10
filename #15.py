"""
This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

"""

# since we don't have an input stream available, I will simply use a list
# we have essentially a random sample of size one. Meaning we need to pick the first element -could be that our stream
# has only length one. Afterwards we add a new element at the i+1th position in stream with probability 1/i+1 because
# stream is of size i+1 and we one random element is chosen with probability 1/i+1
import random


def choose_random(input_stream):
    i = 1
    first_element = input_stream[0]
    while len(input_stream) > 0:
        ran_int = random.randint(0, i)
        if ran_int == i:
            first_element = input_stream[i]
        del input_stream[i]
        i += 1
    return first_element

