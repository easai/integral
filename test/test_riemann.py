""" PyTest files for IntegralRiemann class
"""


from src.integral import *
import pytest


def f(x):
    return x**3


riemann = IntegralRiemann(f)


def test_left_riemann():
    """Test left Riemann sum
    """
    res = riemann.left_riemann(0, 1, 4)
    ans = 0
    for i in range(0, 4):
        x = 1 / 4 * i
        ans += 1 / 4 * f(x)
    print(f"{res=}")
    print(f"{ans=}")
    assert res == ans


def test_right_riemann():
    """Test left Riemann sum
    """
    res = riemann.right_riemann(0, 1, 4)
    ans = 0
    for i in range(1, 5):
        x = 1 / 4 * i
        ans += 1 / 4 * f(x)
    print(f"{res=}")
    print(f"{ans=}")
    assert res == ans


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
