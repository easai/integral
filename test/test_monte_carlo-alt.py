# test_monte_carlo.py
import pytest
import numpy as np
from src.integral import *


@pytest.fixture
def monte_carlo():
    def f(x):
        return x
    return MonteCarlo(f, 0.0, 1.0, 0.5)

@pytest.mark.skip
def test_integration(monte_carlo):
    result = monte_carlo.integrate(1000)
    assert result == pytest.approx(0.5)


def test_error(monte_carlo):
    result = monte_carlo.error(1000)
    assert result < 0.1


def test_difference(monte_carlo):
    result = monte_carlo.find_degree(1e-3)
    assert result < 1000

@pytest.mark.skip
def test_log_message(monte_carlo):
    with pytest.capture.output() as capsys:
        monte_carlo.print_results(1000)
        captured = capsys.read()
    assert captured == "Degree: 1000\r\nApproximation: 0.5\r\nError: 0.0\r\n"
