import math


def gaussian_chebyshev_fixed_range(f, n):
    """Calculate the Gaussian Chebyshev quadrature of degree n over [-1,1]
    """
    w = math.pi/n
    res = 0
    for i in range(1, n+1):
        # Calculate Chebyshev nodes
        x = math.cos((2.0*i-1)/(2*n)*math.pi)
        res += w*f(x)
    return res

a = -1
b = 1
n = 10

def f(x):
    return x**2+1

g = gaussian_chebyshev_fixed_range(f, n)

print(f"{g=}")
print(f"{1.5*math.pi=}")

