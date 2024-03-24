import math


def gaussian_quadrature_3_fixed_range(f):
    """Calculate the gaussian quadrature of degree n=3 over [-1,1]
    """
    w = [5.0/9, 8.0/9, 5.0/9]
    x = [-math.sqrt(3.0/5), 0, math.sqrt(3.0/5)]
    res = 0
    for i in range(len(w)):
        res += w[i]*f(x[i])
    return res


def gaussian_quadrature_3(f, a, b):
    """Calculate the Gaussian quadrature of f(x), degree n=3 over [a,b]
    """
    w = [5.0/9, 8.0/9, 5.0/9]
    x = [-math.sqrt(3.0/5), 0, math.sqrt(3.0/5)]
    res = 0
    A = (b-a)/2.0
    B = (a+b)/2.0
    for i in range(len(w)):
        res += w[i]*f(A*x[i]+B)
    return A*res


a = 1
b = 3

I = math.log(b) - math.log(a)

def f(x):
    return 1/x

g = gaussian_quadrature_3(f, a, b)

print(f"{I=}")
print(f"{g=}")
