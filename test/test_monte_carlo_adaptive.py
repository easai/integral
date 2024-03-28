import pytest
import numpy as np

from src.integral import *


def test_integration():
    def f(x): return x**2
    monte_carlo = MonteCarlo(f, 0.0, 1.0, 1.0/3)
    degree = monte_carlo.find_degree(1e-3)
    res = monte_carlo.integrate(degree)
    assert abs(res - 1.0/3) < 1e-3

def test_integration_non_adaptive():
    def f(x): return x**2
    monte_carlo = MonteCarlo(f, 0.0, 1.0, 1.0/3)
    degree = 10000
    res = monte_carlo.integrate_non_adaptive(degree)
    assert abs(res - 1.0/3) < 1e-3


def test_error():
    def f(x): return x**2
    monte_carlo = MonteCarlo(f, 0.0, 1.0, 1.0/3)
    degree = 1000
    res = monte_carlo.error(degree)
    assert res > 0


def test_find_degree():
    def f(x): return x**2
    monte_carlo = MonteCarlo(f, 0.0, 1.0, 1.0/3)
    degree = monte_carlo.find_degree(1e-3)
    assert degree > 0


def test_print_results():
    def f(x): return x**2
    monte_carlo = MonteCarlo(f, 0.0, 1.0, 1.0/3)
    degree = 1000
    monte_carlo.print_results(degree)


def test_get_var():
    def f(x): return x**2
    monte_carlo = MonteCarlo(f, 0.0, 1.0, 1.0/3)
    var = monte_carlo.get_var(0.0, 1.0, 1000)
    assert var > 0


def test_get_ratio():
    def f(x): return x**2
    monte_carlo = MonteCarlo(f, 0.0, 1.0, 1.0/3)
    ratio = monte_carlo.get_ratio(0.0, 1.0, 1000)
    assert ratio > 0


if __name__ == '__main__':
    pytest.main()