import math
import numpy as np

class GaussHermiteQuadrature:
    """
    A class to perform Gauss-Hermite quadrature.
    """
    def __init__(self, f):
        """
        Initialize the class with the function to integrate.
        """
        self.f = f
        self.approx_values = 0
        self.error_values = 0

    def hermite_nodes_and_weights(self, n):
        """
        Generate nodes and weights for the Gauss-Hermite quadrature of order n.
        """
        return np.polynomial.hermite.hermgauss(n)

    def integrate(self, n):
        """
        Perform the Gauss-Hermite quadrature to approximate the integral of the function.
        """
        x, w = self.hermite_nodes_and_weights(n)
        res = 0
        for i in range(0, len(x)):
            res += w[i]*self.f(x[i])
        self.approx_values=res
        return res

    def error(self, n):
        """
        Calculate the error between the approximation and the exact value.
        """
        approx = self.integrate(n)
        exact = math.sqrt(math.pi/2)
        self.error_values=abs(approx - exact)
        return abs(approx - exact)

    def find_degree(self, tol):
        """
        Find the degree needed to achieve a certain tolerance.
        """
        n = 1
        while self.error(n) > tol:
            n += 1
        return n

    def print_results(self, n):
        """
        Print the degree, approximation, and error.
        """
        print("Degree:", n)
        print("Approximation:", self.approx_values)
        print("Error:", self.error_values)

# Example usage
f = lambda x: math.exp(-x**2)
gauss_hermite = GaussHermiteQuadrature(f)
degree = gauss_hermite.find_degree(1e-6)
gauss_hermite.print_results(degree)