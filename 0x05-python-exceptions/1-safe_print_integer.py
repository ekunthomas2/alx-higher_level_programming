#!/usr/bin/python3
# 1-safe_print_integer.py
# Ekun-Thomas Francisn <ekun_tee@yahoo.com>


def safe_print_integer(value):
    """Print an integer with "{:d}".format().
    Args:
    value (int): The integer to print.
    Returns:
    If a TypeError or ValueError occurs - False.
    Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)