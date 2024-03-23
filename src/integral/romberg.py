import math

def trapezoidal(f, a, b, m):
    n = int(2**m)
    if n==0:
        deltax=(b-a)
    else:
        deltax = (b - a) / n
    domain = [a + x * deltax for x in range(0, n + 1)]
    value = [f(x) for x in domain]
    res = sum(value)
    res -= value[0] * .5
    res -= value[-1] * .5
    res *= deltax
    return res

def romberg(f, a, b, m, k, memo={}):
    key = (a, b, m, k)
    if key in memo:
        return memo[key]
    if k == 0:
        res = trapezoidal(f, a, b, m)
    else:
        res = romberg(f, a, b, m, k-1, memo) - (romberg(f, a, b, m-1, k-1, memo) - romberg(f, a, b, m, k-1, memo))/(4**k-1)
    memo[key] = res
    return res

import math
import numpy as np

def gaussian_function(x):
    return 2 / np.sqrt(math.pi) * np.exp(-x ** 2)

# Define the range of integration
a = 0
b = 1

# Calculate the integral using Romberg's method
m = 3
k = 3
integral = romberg(gaussian_function, a, b, m, k)

# Compare the result with the actual value of erf(1)
actual_value = math.erf(1)

print("Approximate integral: ", integral)
print("Actual integral (erf(1)): ", actual_value)