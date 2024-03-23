import math
import numpy as np

def gaussian_function(x):
    return 2 / np.sqrt(math.pi) * np.exp(-x ** 2)

def trapezoidal(f, a, b, m):
    n = int(2**m)
    deltax = (b - a) / n
    domain = [a + x * deltax for x in range(0, n + 1)]
    value = [f(x) for x in domain]
    res = sum(value)
    res -= value[0] * .5
    res -= value[-1] * .5
    res *= deltax
    return res

def romberg(f, a, b, eps, memo={}):
    # Initialize the maximum number of iterations
    max_iter = 100

    # Initialize the current estimate of the integral
    res = 0

    # Initialize the error estimate
    err = float('inf')

    m=3

    # Loop until the error estimate is less than eps or max_iter is reached
    for k in range(max_iter):
        # Calculate the new estimate of the integral using Romberg's method
        res_new = romberg_iter(f, a, b, m, k, memo)

        # Calculate the error estimate
        err_new = abs(res_new - res)

        # Update the current estimate and error estimate
        res = res_new
        err = err_new

        # If the error estimate is less than eps, stop the loop
        if err < eps:
            break

    return res

def romberg_iter(f, a, b, m, k, memo):
    key = (a, b, m, k)
    if key in memo:
        return memo[key]
    if k == 0:
        res = trapezoidal(f, a, b, m)
    else:
        res = romberg_iter(f, a, b, m, k-1, memo) - (romberg_iter(f, a, b, m-1, k-1, memo) - romberg_iter(f, a, b, m, k-1, memo))/(4**k-1)
    memo[key] = res
    return res


# Define the range of integration
a = 0
b = 1

# Define the desired precision
eps = 1e-6

# Calculate the integral using the adaptive Romberg's method
integral = romberg(gaussian_function, a, b, eps)

print("Approximate integral: ", integral)


