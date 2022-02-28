from random import randint
from check_time import adder_cython, subtractor_cython, adder_py, subtractor_py


def random_with_N_digits(n):
    for _ in range(n):
        range_start = 10 ** (n - 1)
        range_end = (10**n) - 1
        yield randint(range_start, range_end)


def test_equality():
    """
    Testing the equality of the results of the two functions
    """
    a, b = (x for x in random_with_N_digits(6)), (x for x in random_with_N_digits(6))
    for x, y in zip(a, b):
        assert adder_cython(x, y) == adder_py(x, y)
        assert subtractor_cython(x, y) == subtractor_py(x, y)
