#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""https://projecteuler.net/problem=2"""


__author__ = "Stanislav D. Kudriavtsev"


import pytest

from id002 import Fibonacci as Fib
from id002 import (solve_problem2 as sp2,
                   solve_problem2_v2 as sp22,
                   solve_problem2_v3 as sp23)


def test_fib1():
    """Test first Fibonacci number."""
    assert Fib().fib1 == 0
    assert Fib(1).fib1 == 1
    with pytest.raises(TypeError):
        Fib("1")
    with pytest.raises(TypeError):
        Fib(0.0)
    with pytest.raises(ValueError):
        Fib(-1)
    with pytest.raises(ValueError):
        Fib(2)


def test_ten_fibs_from_zero():
    """List first 10 Fibonacci numbers starting from 0."""
    fib = Fib()
    fibs = [next(fib) for i in range(10)]
    assert fibs == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_ten_fibs_from_one():
    """List first 10 Fibonacci numbers starting from 1."""
    fib = Fib(1)
    fibs = [next(fib) for i in range(10)]
    assert fibs == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_ten_fibs_from_one_and_two():
    """List first 10 Fibonacci numbers starting from 1 and 2."""
    fib = Fib()
    fibs = [next(fib) for i in range(12)]
    assert fibs[2:] == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_problem2_solution():
    """Problem 2 solution."""
    tdata = {10: 10, 100: 44, 4e6: 4613732}
    for num, res in tdata.items():
        assert sp2(num) == res
        assert sp22(num) == res
        assert sp23(num) == res
