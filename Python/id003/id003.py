#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""https://projecteuler.net/problem=3"""


__author__ = "Stanislav D. Kudriavtsev"


from collections import Counter
from math import sqrt


def is_natural(num: int):
    """Test if the number is natural."""
    if not (isinstance(num, int) and num > 0):
        return False
    return True


# an attempt to do without factors list passed in Counter object
def factorise(num: int):
    """Return the list of factors of the natural number.

    Parameters
    ----------
    num : int
        natural number to factorise

    Returns
    -------
    prime factors with their powers : dict
    """

    def get_limit(num: int):
        """Return the closest upper integer of sqrt(num)."""
        return int(sqrt(num)) + 1

    def reduce(num1: int, num2: int):
        """If num1 % num2 == 0, num1 is reduced by the amount of num2 in num1.

        The global factors dictionary is updated with num2 subfactors of num1. 
        """
        dnums: list = []
        while not num1 % num2:
            dnums.append(num2)
            num1 //= num2
        if dnums:
            nonlocal factors  # type: ignore
            factors.update({num2: len(dnums)})
        return num1

    factors = {}  # see reduce inner function
    if is_natural(num):
        num = reduce(num, 2)  # even components reduced
        dnum = 3
        maxlim = get_limit(num)
        while dnum <= maxlim:
            num = reduce(num, dnum)
            maxlim = get_limit(num)
            dnum += 2
        if num > 1:
            factors[num] = 1  # add the rest
    return factors


def solve_problem3(num: int):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143?
    """
    # Costly. A good way to find the lowest prime and its power
    # and then just divide the number by prime**power
    factors = factorise(num)
    if factors:
        return max(factors)
    return None


if __name__ == "__main__":
    print(solve_problem3(13195))
    print(solve_problem3(600851475143))
