from src.integral import *
import pytest
from math import *


def f(x):
    return sqrt(x)

trapezoidal=IntegralTrapezoidal()

def test_trapezoidal():
    res=trapezoidal.trapezoidal(f,0,10000,10000)
    sum=0
    for i in range(0,10001):
        sum+=sqrt(i)
    res+=50
    print(f"{sum=}")
    print(f"{res=}")
    assert sum==res
