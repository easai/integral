from src.integral import *
import pytest
import numpy as np
import math


@pytest.fixture
def glq():
    def f(x): return math.exp(-x)
    exact = 0.5
    return GaussLaguerreQuadrature(f, exact)


def test_integration(glq):
    degree = 10
    x, w = glq.laguerre_nodes_and_weights(degree)
    res = 0
    for i in range(0, len(x)):
        res += w[i]*glq.f(x[i])
    assert abs(res - glq.exact) < 1e-6


def test_find_degree(glq):
    tol = 1e-6
    degree = glq.find_degree(tol)
    assert degree > 0
    assert glq.error(degree) < tol


def test_print_results(glq):
    degree = 10
    glq.print_results(degree)
