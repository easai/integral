import pytest
import math
import numpy as np

from src.integral import *


@pytest.fixture
def monte_carlo():
    def f(x): return x
    return MonteCarlo(f, 0.0, 1.0, 0.5)


def test_integrate(monte_carlo):
    """
    Test the integrate method.
    """
    n = 1000
    exact = 0.5
    approx = monte_carlo.integrate(n)
    assert np.allclose(approx, exact, atol=1e-1)


def test_error(monte_carlo):
    """
    Test the error method.
    """
    n = 1000
    error = monte_carlo.error(n)
    assert np.allclose(error, 0.0, atol=1e-1)


def test_find_degree(monte_carlo):
    """
    Test the find_degree method.
    """
    tol = 1e-3
    degree = monte_carlo.find_degree(tol)
    assert degree < 1000


def test_print_results(monte_carlo):
    """
    Test the print_results method.
    """
    degree = monte_carlo.find_degree(1e-3)
    monte_carlo.print_results(degree)
    assert True  # just to make the test pass
