""" PyTest files for IntegralRiemann class
"""


from src.integral import *
import pytest
from math import *


def f(x):
    return x**3


riemann = IntegralRiemann()


def test_right_riemann():
    """Test right Riemann sum
    """
    res = riemann.right_riemann(f, 0, 1, 4)
    ans = 0
    for i in range(1, 5):
        x = 1 / 4 * i
        ans += 1 / 4 * f(x)
    print(f"\n{riemann.right_riemann(f, 0, 1, 4)=}")
    assert res == ans


def test_left_riemann():
    """Test left Riemann sum
    """
    res = riemann.left_riemann(f, 0, 1, 4)
    ans = 0
    for i in range(0, 4):
        x = 1 / 4 * i
        ans += 1 / 4 * f(x)
    print(f"\n{riemann.left_riemann(f, 0, 1, 4)=}")
    assert res == ans


def g(x):
    return sin(pi * x) + 37 * x**3


def test_left_riemann_g():
    r = IntegralRiemann()
    res = r.left_riemann(g, 0, 1, 4)
    print(f"\ng(x)=sin(pi*x)+37*x^3: {res}")
    ans = (1 + sqrt(2)) / 4 + 37 * riemann.left_riemann(f, 0, 1, 4)
    assert abs(ans - res) < 1e-6

# def test_left_riemann_err(self):
# if self.verbose:
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
