from src.integral import *
import pytest
from math import *


def g(x):
    return sin(x)

def f(x):
    return 1/x

def ff(x):
    return 2/x**3

trapezoidal=IntegralTrapezoidal()


def test_trapezoidal_4():
    res=trapezoidal.trapezoidal(g,0,pi,4)
    ans=pi*(sqrt(2)+1)/4
    assert (res-ans)<13-6

def test_trapezoidal():
    res = trapezoidal.trapezoidal(g,0,pi,2)
    ans=pi/2
    assert (res-ans)<13-6

def test_ln():
    res=trapezoidal.trapezoidal(f,1,2,2)
    ans=17/24
    assert (res-ans)<1e-6

def test_err():
    res = trapezoidal.trapezoidal_n(ff,1,2,1000,1e-6)
    assert res==409
