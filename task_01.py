#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 Synthesizing Task 01"""


def xfibo(count):
    """Fibo sequence generation function.
    Args:
        count(int): Number of integers to return in the sequence.
    Returns: A list of Fibonacci numbers.
    Examples:
        >>> for i in xfibo(5):
                print i
        0
        1
        1
        2
        3
    """
    iteration = 0
    lastnum, curnum = 0, 1
    while iteration < count:
        yield lastnum
        lastnum, curnum = curnum, lastnum + curnum
        iteration += 1
