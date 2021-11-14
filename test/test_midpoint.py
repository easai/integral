from src.integral import *
import pytest
from math import *


def f(x):
    return 1/x

def ff(x):
    return 2/x**3

midpoint=IntegralMidpoint()

def test_mid():
    res=midpoint.midpoint_n(ff,1,2,1000,1e-6)
    assert res==289

def g(x):
    return e**(x/2)

def test_estimate():
    res=midpoint.midpoint(g,0,1,100)
    ans=2*(sqrt(e)-1)
    assert res<ans
