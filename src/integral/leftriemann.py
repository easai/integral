"""Use the left Riemann Rule to approximate integral

Usage: left-riemann.py [--test|-t] [--help|-h] [--verbose|-v]

Options:
	-h --help	show this help message and exit
	-t --test	perform unit test
	-v --verbose	verbose mode
"""
import unittest
from docopt import docopt
from math import *


class IntegralLeftRiemann():
    def __init__(self):
        pass

    def left_riemann(self, f, a, b, n):
        """ Approximate integral of f on the interval [a,b] over n subintervals using the left Riemann rule
        """
        deltax = (b - a) / n
        domain = [a + x * deltax for x in range(0, n)]
        value = [f(x) for x in domain]
        res = sum(value)
        res *= deltax
        return res

    def left_riemann_n(self, ff, a, b, n, limit):
        """ Obtain the minimum number of subintervals n with the error under limit using the left Riemann rule
        """
        deltax = (b - a) / n
        domain = [a + x * deltax for x in range(0, n + 1)]
        value = [ff(x) for x in domain]
        maxff = max(value)
        return ceil(sqrt(maxff * (b - a)**3 / (24 * limit)))

    def left_riemann_err(self, ff, a, b, n):
        """ Calculate the max error guaranteed by the left Riemann Rule
        """
        deltax = (b - a) / n
        domain = [a + x * deltax for x in range(0, n + 1)]
        value = [ff(x) for x in domain]
        maxff = max(value)
        return maxff * (b - a)**3 / (24 * n**2)


class TestLeftRiemann(unittest.TestCase):
    verbose = False
    integral = IntegralLeftRiemann()

    def f(self, x):
        if x == 0:
            return 0
        return 1 / x

    def ff(self, x):
        if x == 0:
            return 0
        return 2 / x**3

    # def test_left_riemann(self):
    # 	res = left_riemann(self.f, 1, 2, 2)
    # 	if self.verbose:
    # 		print("\nApproximating the integral using the left Riemann rule")
    # 		print(f"{res=}")
    # 		print(f"{24/35=}")
    # 	self.assertTrue(abs(res - 24/35) < 1e-5)
    #
    # def test_left_riemann_err(self):
    # 	n = 289
    # 	err = left_riemann_err(self.ff, 1, 2, n)
    # 	if self.verbose:
    # 		print("\nThe error margin")
    # 		print(f"{n=}")
    # 		print(f"{err=}")
    # 	self.assertTrue(err < 1e-6)
    #
    # def test_left_riemann_n(self):
    # 	limit = 1e-6
    # 	n = 289
    # 	n = left_riemann_n(self.ff, 1, 2, n, limit)
    # 	err = left_riemann_err(self.ff, 1, 2, n)
    # 	if self.verbose:
    # 		print("\nThe minimum number of subintervals n")
    # 		print(f"{limit=}")
    # 		print(f"{n=}")
    # 		print(f"{err=}")
    # 	self.assertTrue(err < limit)

    def g(self, x):
        return 1 / (1 + x * x)

    def test_g(self):
        res = self.integral.left_riemann(self.g, 0, 1, 4)
        print(f"{res=}")


if __name__ == '__main__':
    args = docopt(__doc__)
    if args['--verbose'] or args['-v']:
        TestLeftRiemann.verbose = True
    if args["--test"] or args["-t"]:
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
