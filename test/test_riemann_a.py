from src.integral import *
import pytest
from math import *


def f(x):
    return x


riemann=IntegralRiemann(f)


def test_left():
    res=riemann.left_riemann(0,1,3)
    assert res==1/3

def test_right():
    res=riemann.right_riemann(0,1,3)
    assert res==2/3


midpoint=IntegralMidpoint()

def test_mid():
    res=midpoint.midpoint(f,0,1,3)
    assert res==1/2
