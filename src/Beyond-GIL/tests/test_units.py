import unittest
from random import randint
from check_time import adder_cython, subtractor_cython, adder_py, subtractor_py


class TestEquality(unittest.TestCase):

    def random_with_N_digits(self, n):
        for _ in range(n):
            range_start = 10 ** (n - 1)
            range_end = (10**n) - 1
            yield randint(range_start, range_end)

    def test_equality(self):
        """
        Testing the equality of the results of the two functions
        """
        a, b = iter(self.random_with_N_digits(6)), iter(self.random_with_N_digits(6))
        for x, y in zip(a, b):
            self.assertEqual(adder_cython(x, y), adder_py(x, y))
            self.assertEqual(subtractor_cython(x, y), subtractor_py(x, y))


if __name__ == '__main__':
    unittest.main()
