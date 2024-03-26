import math
from sympy import *

class GaussLaguerreQuadrature:
    """
    A class to perform Gauss-Laguerre quadrature.
    """
    def __init__(self, f, exact):
        """
        Initialize the class with the function to integrate.
        """
        self.f = f
        self.exact = exact
        self.approx_value = 0
        self.error_value = 0

    def laguerre_nodes_and_weights(self, n):
        """
        Generate nodes and weights for the Gauss-Laguerre quadrature of order n.
        """
        x = Symbol("x")
        roots = Poly(laguerre(n, x)).all_roots()
        x_i = [rt.evalf(20) for rt in roots]
        w_i = [(rt / ((n + 1) * laguerre(n + 1, rt)) ** 2).evalf(20) for rt in roots]
        return x_i, w_i

    def integrate(self, n):
        """
        Perform the Gauss-Laguerre quadrature to approximate the integral of the function.
        """
        x, w = self.laguerre_nodes_and_weights(n)
        res = 0
        for i in range(0, len(x)):
            res += w[i]*self.f(x[i])
        self.approx_value=res
        return res

    def error(self, n):
        """
        Calculate the error between the approximation and the exact value.
        """
        approx = self.integrate(n)
        self.error_value=abs(approx - self.exact)
        return abs(approx - self.exact)

    def find_degree(self, tol):
        """
        Find the degree needed to achieve a certain tolerance.
        """
        n = 1
        max_iter=10
        while self.error(n) > tol and n<max_iter:
            n += 1
        return n

    def print_results(self, n):
        """
        Print the degree, approximation, and error.
        """
        print("Degree:", n)
        print("Approximation:", self.approx_value)
        print("Error:", self.error_value)

# Example usage
f = lambda x: math.exp(-x)
gauss_hermite = GaussLaguerreQuadrature(f, .5)
degree = gauss_hermite.find_degree(1e-6)
gauss_hermite.print_results(degree)

