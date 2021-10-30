""" PyTest files for integral
"""


from src.integral import *
import pytest


verbose = False
integral = IntegralTrapezoidal()


def f(x):
    if x == 0:
        return 0
    return 1 / x


def ff(x):
    if x == 0:
        return 0
    return 2 / x**3


def test_trapezoidal():
    res = integral.trapezoidal(f, 1, 2, 2)
    if verbose:
        print("\nApproximating the integral using the trapezoidal rule")
        print(f"{res=}")
        print(f"{17/24=}")
    assert abs(res - 17 / 24) < 1e-6


def test_trapezoidal_err():
    n = 409
    err = integral.trapezoidal_err(ff, 1, 2, n)
    if verbose:
        print("\nThe error margin")
        print(f"{n=}")
        print(f"{err=}")
    assert err < 1e-6


def test_trapezoidal_n():
    limit = 1e-6
    n = 400
    n = integral.trapezoidal_n(ff, 1, 2, n, limit)
    err = integral.trapezoidal_err(ff, 1, 2, n)
    if verbose:
        print("\nThe minimum number of subintervals n")
        print(f"{limit=}")
        print(f"{n=}")
        print(f"{err=}")
    assert err < limit


def g(x):
    return 1 / (1 + x * x)


def test_g():
    res = integral.trapezoidal(g, 0, 1, 4)
    print(f"{res=}")
