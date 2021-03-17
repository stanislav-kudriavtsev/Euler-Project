#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""https://projecteuler.net/problem=1"""


__author__ = "Stanislav D. Kudriavtsev"


def posint(num: int):
    """Ensure the num is natural, that is positive integer."""
    if not isinstance(num, int):
        raise TypeError("number must be integer")
    if num <= 0:
        raise ValueError("number must be positive")


# first inefficient naive solution
def solve_problem1(num: int):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    posint(num)
    return sum(n for n in range(1, num) if not (n % 3) or not (n % 5))


### improved version

# We can form two distinct sequences of numbers - multiples of 3 and 5.
# So their sum will automatically compose the needed sum
# But, nultiples of both 3 and 5, that is 15, can be in both sequences.
# That is the reason to count them and subtract from the total sum
# to avoid overcounting.


def solve_problem1_v2(num: int):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """

    def sum_seq(dnum: int):
        """sum the sequence of numbers below bnum and multiples of dnum."""
        posint(dnum)
        nonlocal num
        last_in = num - 1  # up to this boundary below num
        last_in = (last_in - (last_in % dnum)) // dnum
        # return the arithmetic progression sum
        return dnum * (last_in * (last_in + 1)) // 2

    posint(num)
    return sum_seq(3) + sum_seq(5) - sum_seq(15)


if __name__ == "__main__":
    print(solve_problem1(1000))
    print(solve_problem1_v2(1000))
