#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""https://projecteuler.net/problem=3"""


__author__ = "Stanislav D. Kudriavtsev"


from id003 import factorise, is_natural
from id003 import solve_problem3 as sp3


def test_is_natural():
    """Test objects on being natural numbers."""
    assert not is_natural(-1)
    assert not is_natural(0)
    assert not is_natural(1.0)
    assert is_natural(1)


def test_factorise_inappropriate_objects():
    """Only natural numbers > 1 are taken into process."""
    assert factorise(-1) == {}
    assert factorise(0) == {}
    assert factorise(1) == {}
    assert factorise(2.3) == {}
    assert factorise([5]) == {}


def test_factorise_numbers():
    """Only natural numbers > 1 are taken into process."""
    assert factorise(2) == {2: 1}
    assert factorise(3) == {3: 1}
    assert factorise(4) == {2: 2}
    assert factorise(10) == {2: 1, 5: 1}
    assert factorise(24) == {2: 3, 3: 1}
    assert factorise(30) == {2: 1, 3: 1, 5: 1}
    assert factorise(32) == {2: 5}
    assert factorise(41) == {41: 1}
    assert factorise(48) == {2: 4, 3: 1}
    assert factorise(60) == {2: 2, 3: 1, 5: 1}


def test_problem3():
    """Prime factors of numbers from the task"""
    assert sp3(0) is None 
    assert sp3(1) is None
    assert sp3(2) == 2
    assert sp3(4) == 2
    assert sp3(6) == 3
    assert sp3(7) == 7
    assert sp3(121) == 11
    assert sp3(13195) == 29
    assert sp3(600851475143) == 6857
