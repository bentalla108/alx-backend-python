#!/usr/bin/env python3

"""
Module: math_operations

Description:
This module provides various mathematical operations
including the 'floor' function.

Functions:
- floor(x: float) -> int: Returns the largest integer
that is less than or equal to 'x'.
"""

import math

def floor(x: float) -> int:
    """
    Function: floor()

    Description:
    Returns the largest integer that is less than or equal to
    the input floating-point number 'x'.

    Parameters:
    - x (float): The floating-point number for which the floor
    value is to be calculated.

    Return Type:
    int: The largest integer that is less than or equal to 'x'.
    """
    return math.floor(x)
