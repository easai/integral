"""Use the Trapezoidal Rule to approximate integral

Usage: trapezoidal.py [--test|-t] [--help|-h] [--verbose|-v]

Options:
	-h --help	show this help message and exit
	-t --test	perform unit test
	-v --verbose	verbose mode
"""
import unittest
from docopt import docopt
from math import *


class IntegralTrapezoidal():
    def __init__(self):
        pass

    def trapezoidal(self, f, a, b, n):
        """ Use the Trapezoidal Rule to approximate integral of f on the interval [a,b] over n subintervals
        """
        deltax = (b - a) / n
        domain = [a + x * deltax for x in range(0, n + 1)]
        value = [f(x) for x in domain]
        res = sum(value)
        res -= value[0] * .5
        res -= value[-1] * .5
        res *= deltax
        return res

    def trapezoidal_n(self, ff, a, b, n, limit):
        """ Obtain the minimum number of subintervals n with the error under limit
        """
        deltax = (b - a) / n
        domain = [a + x * deltax for x in range(0, n + 1)]
        value = [ff(x) for x in domain]
        maxff = max(value)
        return ceil(sqrt(maxff * (b - a)**3 / (12 * limit)))

    def trapezoidal_err(self, ff, a, b, n):
        """ Calculate the max error guaranteed by the Trapezoidal Rule
        """
        deltax = (b - a) / n
        domain = [a + x * deltax for x in range(0, n + 1)]
        value = [ff(x) for x in domain]
        maxff = max(value)
        return maxff * (b - a)**3 / (12 * n * n)


class TestTrapezoidal(unittest.TestCase):
    verbose = False
    integral = IntegralTrapezoidal()

    def f(self, x):
        if x == 0:
            return 0
        return 1 / x

    def ff(self, x):
        if x == 0:
            return 0
        return 2 / x**3

    def test_trapezoidal(self):
        res = self.integral.trapezoidal(self.f, 1, 2, 2)
        if self.verbose:
            print("\nApproximating the integral using the trapezoidal rule")
            print(f"{res=}")
            print(f"{17/24=}")
        self.assertTrue(abs(res - 17 / 24) < 1e-6)

    def test_trapezoidal_err(self):
        n = 409
        err = self.integral.trapezoidal_err(self.ff, 1, 2, n)
        if self.verbose:
            print("\nThe error margin")
            print(f"{n=}")
            print(f"{err=}")
        self.assertTrue(err < 1e-6)

    def test_trapezoidal_n(self):
        limit = 1e-6
        n = 400
        n = self.integral.trapezoidal_n(self.ff, 1, 2, n, limit)
        err = self.integral.trapezoidal_err(self.ff, 1, 2, n)
        if self.verbose:
            print("\nThe minimum number of subintervals n")
            print(f"{limit=}")
            print(f"{n=}")
            print(f"{err=}")
        self.assertTrue(err < limit)

    def g(self, x):
        return 1 / (1 + x * x)

    def test_g(self):
        res = self.integral.trapezoidal(self.g, 0, 1, 4)
        print(f"{res=}")


if __name__ == '__main__':
    args = docopt(__doc__)
    if args['--verbose'] or args['-v']:
        TestTrapezoidal.verbose = True
    if args["--test"] or args["-t"]:
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
