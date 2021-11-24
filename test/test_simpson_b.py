from src.integral import *
import pytest
from math import *


def f(x):
    return cos(x*x)

def f4(x):
    return 16*(x**4)*cos(x*x)+48*x*x*sin(x*x)-12*cos(x*x)


simpson=IntegralSimpson()

x=sqrt(pi/2)


def test_simpson_4():
    res=simpson.simpson(f,0,x,4)
    print(f"4: {res=}")


def test_simpson_8():
    res=simpson.simpson(f,0,x,8)
    print(f"8: {res=}")


def test_simpson_err():
    res = simpson.simpson_n(f4,0,x,1000,1e-6)
    print(f"n: {res=}")


def test_simpson_34():
    for n in range(15,45):
        res=simpson.simpson(f,0,x,n)
        print(f"{n}: {res=}")
