#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 Synthesizing Task 02."""

import task_01


def fibo(count):
    """Returns Fibonacci numbers.
    Args:
        count(int): The total number of Fibonacci numbers to return.
    Returns: List of Fibonacci numbers.
    Examples:
        >>> fibo(5)
        [0, 1, 1, 2, 3]
    """
    return [num for num in task_01.xfibo(count)]
