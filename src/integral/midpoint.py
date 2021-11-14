"""Use the midpoint Rule to approximate integral

Usage: midpoint.py [--test|-t] [--help|-h] [--verbose|-v]

Options:
    -h --help	show this help message and exit
    -t --test	perform unit test
    -v --verbose	verbose mode
"""
import unittest
from docopt import docopt
from math import *


class IntegralMidpoint():
    def __init__(self):
        pass

    def midpoint(self, f, a, b, n):
        """ Approximate integral of f on the interval [a,b] over n subintervals using the midpoint rule
        """
        deltax = (b - a) / n
        domain = [a + x * deltax for x in range(0, n + 1)]
        value = [f(x + deltax * .5) for x in domain[:-1]]
        res = sum(value)
        res *= deltax
        return res

    def midpoint_n(self, ff, a, b, n, limit):
        """ Obtain the minimum number of subintervals n with the error under limit using the midpoint rule

        Args:
            ff(function): f''(x)

    """
        deltax = (b - a) / n
        domain = [a + x * deltax for x in range(0, n + 1)]
        value = [ff(x) for x in domain]
        maxff = max(value)
        return ceil(sqrt(maxff * (b - a)**3 / (24 * limit)))

    def midpoint_err(self, ff, a, b, n):
        """ Calculate the max error guaranteed by the midpoint Rule
        """
        deltax = (b - a) / n
        domain = [a + x * deltax for x in range(0, n + 1)]
        value = [ff(x) for x in domain]
        maxff = max(value)
        return maxff * (b - a)**3 / (24 * n**2)


class Testmidpoint(unittest.TestCase):
    verbose = False
    integral = IntegralMidpoint()

    def f(self, x):
        if x == 0:
            return 0
        return 1 / x

    def ff(self, x):
        if x == 0:
            return 0
        return 2 / x**3

    def test_midpoint(self):
        res = self.integral.midpoint(self.f, 1, 2, 2)
        if self.verbose:
            print("\nApproximating the integral using the midpoint rule")
            print(f"{res=}")
            print(f"{24/35=}")
        self.assertTrue(abs(res - 24 / 35) < 1e-5)

    def test_midpoint_err(self):
        n = 289
        err = self.integral.midpoint_err(self.ff, 1, 2, n)
        if self.verbose:
            print("\nThe error margin")
            print(f"{n=}")
            print(f"{err=}")
        self.assertTrue(err < 1e-6)

    def test_midpoint_n(self):
        limit = 1e-6
        n = 289
        n = self.integral.midpoint_n(self.ff, 1, 2, n, limit)
        err = self.integral.midpoint_err(self.ff, 1, 2, n)
        if self.verbose:
            print("\nThe minimum number of subintervals n")
            print(f"{limit=}")
            print(f"{n=}")
            print(f"{err=}")
        self.assertTrue(err < limit)


if __name__ == '__main__':
    args = docopt(__doc__)
    if args['--verbose'] or args['-v']:
        Testmidpoint.verbose = True
    if args["--test"] or args["-t"]:
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
