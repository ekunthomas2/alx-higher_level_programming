#!/usr/bin/python3
# 3-safe_print_division.py
# Ekun-Thomas Francis <ekun_tee@yahoo.com>


def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
