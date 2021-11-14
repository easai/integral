from src.integral import *
import pytest
from math import *


def g(x):
    return sin(x)

def f(x):
    return 1/x

def f4(x):
    return 24/x**5

simpson=IntegralSimpson()


def test_simpson_4():
    res=simpson.simpson(g,0,pi,4)
    ans=pi*(4/sqrt(2)+1)/6
    assert (res-ans)<13-6

def test_simpson():
    res = simpson.simpson(g,0,pi,2)
    ans=pi*2/3
    assert (res-ans)<13-6

def test_simpson_ln():
    res=simpson.simpson(f,1,2,2)
    ans=25/36
    assert (res-ans)<1e-6

def test_simpson_err():
    res = simpson.simpson_n(f4,1,2,1000,1e-6)
    assert res==20

def g(x):
    return 1/(3*sqrt(2*pi))*exp(-(x-64)**2/18)

def test_normal():
    res = simpson.simpson(g,64,68,4)
    print(f"{res=}")
