#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""https://projecteuler.net/problem=2"""


__author__ = "Stanislav D. Kudriavtsev"


from itertools import cycle, takewhile


class Fibonacci:
    """Fibonacci sequence iterator."""

    def __init__(self, fib1: int = 0):
        if not isinstance(fib1, int):
            raise TypeError("Fibonacci numbers can be only integers.")
        if fib1 not in (0, 1):
            raise ValueError("the first Fibonacci can be only 0 or 1.")
        self.fib1, self.fib2 = fib1, 1

    def __iter__(self):
        return self

    def __next__(self):
        current = self.fib1
        self.fib1, self.fib2 = self.fib2, self.fib1 + self.fib2
        return current


def solve_problem2(uplimit: int):
    """
    Each new term in the Fibonacci sequence is generated
    by adding the previous two terms. By starting with 1 and 2,
    the first 10 terms will be:

        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence
    whose values do not exceed four million,
    find the sum of the even-valued terms.
    """
    fibiter = Fibonacci(1)
    next(fibiter)  # get rid of the first 1
    return sum(
        fib for fib in takewhile(lambda x: (x <= uplimit), fibiter) if not fib % 2
    )


# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# 0, 1, 2, 0, 1, 2, 0 , 1 , 2 , ...
# Every third Fibonacci number is even, is it?
# F(1st) = 1, F(2nd) = 1 -> F(3d) = 1 + 1 = 2
# then 2l [current] + (2k + 1) [previous] -> odd [2(k + l) + 1]
# then current odd and previous even -> still odd
# but on the next third value + odd to the already odd current -> even


def solve_problem2_v2(uplimit: int):
    """
    Each new term in the Fibonacci sequence is generated
    by adding the previous two terms. By starting with 1 and 2,
    the first 10 terms will be:

        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence
    whose values do not exceed four million,
    find the sum of the even-valued terms.
    """
    fibiter = Fibonacci(1)
    fibsum = 0
    while True:
        for _ in range(2):
            next(fibiter)
        fibel = next(fibiter)  # even
        if fibel > uplimit:
            break
        fibsum += fibel
    return fibsum


# Hacker Rank
def solve_problem2_v3(uplimit: int):
    fsum, fel1, fel2 = 0, 0, 2
    while fel2 < uplimit:
        fsum, fel1, fel2 = fsum + fel2, fel2, 4 * fel2 + fel1
    return fsum


if __name__ == "__main__":
    print(solve_problem2())
    print(solve_problem2_v2())
    print(solve_problem2_v3())
