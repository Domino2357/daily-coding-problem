"""
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2
"""

# had to google what a Monte Carlo method is: essentially one creates random points .
import random
from math import sqrt

# if r == 1, the area becomes pi
import numpy


def pi_estimator(number_of_digits):
    number_inside = 0
    number_outside = 0
    for i in range(0, number_of_digits):
        x = numpy.random.rand()
        y = numpy.random.rand()
        if is_inside(x, y):
            number_inside += 1
        else:
            number_outside += 1
    return 4 * number_inside / (number_outside + number_inside)


def is_inside(x, y):
    if x * x + y * y < 1.0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(pi_estimator(9000000))
