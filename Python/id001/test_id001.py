#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""https://projecteuler.net/problem=1"""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import raises

from id001 import solve_problem1 as sp1, solve_problem1_v2 as sp12


def test_problem1_failures():
    """Only natural numbers for solving problems."""
    for failval in "-2", -1, 0, [1]:
        with raises((TypeError, ValueError)):
            assert sp1(failval)
            assert sp12(failval)


def test_problem1_10():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.
    """
    assert sp1(10) == 23
    assert sp12(10) == 23


def test_problem1_100():
    """Find the sum of all the multiples of 3 or 5 below 100."""
    assert sp1(100) == 2318
    assert sp12(100) == 2318


def test_problem1_solution():
    """Find the sum of all the multiples of 3 or 5 below 1000."""
    assert sp1(1000) == 233168
    assert sp12(1000) == 233168
