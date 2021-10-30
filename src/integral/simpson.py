"""Use the Simpson Rule to approximate integral

Usage: simpson.py [--test|-t] [--help|-h] [--verbose|-v]

Options:
	-h --help	show this help message and exit
	-t --test	perform unit test
	-v --verbose	verbose mode
"""
import unittest
from docopt import docopt
from math import *


class IntegralSimpson():
    def __init__(self):
        pass

    def simpson(self, f, a, b, n):
        """ Approximate integral of f on the interval [a,b] over n subintervals using the Simplson's rule
        """
        deltax = (b - a) / n
        domain = [a + x * deltax for x in range(0, n + 1)]
        print(domain)
        res = sum([4 * f(x) for x in domain[1:-1]])
        res -= sum([2 * f(x) for x in domain[1:-1][1:-1][0::2]])
        res += f(domain[0])
        res += f(domain[-1])
        res *= deltax / 3
        return res

    def simpson_n(self, f4, a, b, n, limit):
        """ Obtain the minimum number of subintervals n with the error under limit using the Simplson's rule
        """
        deltax = (b - a) / n
        domain = [a + x * deltax for x in range(0, n + 1)]
        value = [f4(x) for x in domain]
        maxff = max(value)
        return ceil((maxff * (b - a)**5 / (180 * limit))**(1 / 4))

    def simpson_err(self, f4, a, b, n):
        """ Calculate the max error guaranteed by the Simpson Rule
        """
        deltax = (b - a) / n
        domain = [a + x * deltax for x in range(0, n + 1)]
        value = [f4(x) for x in domain]
        maxff = max(value)
        print(f"{maxff=}")
        return maxff * (b - a)**5 / (180 * n**4)


class TestSimpson(unittest.TestCase):
    verbose = False
    integral = IntegralSimpson()

    def f(self, x):
        if x == 0:
            return 0
        return 1 / x

    def f4(self, x):
        if x == 0:
            return 0
        return 24 / x**5

    def test_simpson(self):
        res = self.integral.simpson(self.f, 1, 2, 2)
        if self.verbose:
            print("\nApproximating the integral using the simpson rule")
            print(f"{res=}")
            print(f"{25/36=}")
        self.assertTrue(abs(res - 25 / 36) < 1e-6)

    def test_simpson_err(self):
        n = 20
        err = self.integral.simpson_err(self.f4, 1, 2, n)
        if self.verbose:
            print("\nThe error margin")
            print(f"{n=}")
            print(f"{err=}")
        self.assertTrue(err < 1e-6)

    def test_simpson_n(self):
        limit = 1e-6
        n = 20
        n = self.integral.simpson_n(self.f4, 1, 2, n, limit)
        err = self.integral.simpson_err(self.f4, 1, 2, n)
        if self.verbose:
            print("\nThe minimum number of subintervals n")
            print(f"{limit=}")
            print(f"{n=}")
            print(f"{err=}")
        self.assertTrue(err < limit)

    def g(self, x):
        return 1 / (1 + x * x)

    def test_g(self):
        res = self.integral.simpson(self.g, 0, 1, 4)
        print(f"{res=}")

    def fresnel(self, x):
        return cos(x * x)

    def fresnel4(self, x):
        return 16 * (x**4) * cos(x * x) + 48 * x * x * sin(x * x) - 12 * cos(x * x)

    def test_fresnel(self):
        pass

    def normal(self, x):
        res = exp(-(x - 64)**2 / 18) / (3 * sqrt(2 * pi))
        if res == 0:
            return 0
        return res

    def test_normal(self):
        res = self.integral.simpson(self.normal, 64, 68, 4)
        err = (1 + 4 * exp(-1 / 18) + 2 * exp(-4 / 18) + 4 *
               exp(-9 / 18) + exp(-16 / 18)) / (9 * sqrt(2 * pi))
        if self.verbose:
            print("\nApproximating the integral using the simpson rule")
            print(f"{res=}")
            print(f"{err=}")
        self.assertTrue(abs(res - err) < 1e1)


if __name__ == '__main__':
    args = docopt(__doc__)
    if args['--verbose'] or args['-v']:
        TestSimpson.verbose = True
    if args["--test"] or args["-t"]:
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
