from src.integral import *
import pytest
from math import *


def f(x):
    return 1 / (1 + x * x)


def test_mid():
    mid = IntegralMidpoint()
    res_mid = mid.midpoint(f, 0, 1, 4)
    print(f"{res_mid=}")


def test_trap():
    trap = IntegralTrapezoidal()
    res_trap = trap.trapezoidal(f, 0, 1, 4)
    print(f"{res_trap=}")


def test_simpson():
    simpson = IntegralSimpson()
    res_simpson = simpson.simpson(f, 0, 1, 4)
    print(f"{res_simpson=}")
