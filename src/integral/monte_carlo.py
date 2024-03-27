import math
import numpy as np
import logging


class MonteCarlo:
    """
    A class to perform MonteCarlo.
    """

    def __init__(self, f, a, b, exact, max_iter=1000, seed=None):
        """
        Initialize the class with the function to integrate.
        """
        self.f = f
        self.a = a
        self.b = b
        self.exact = exact
        self.max_iter = 1000
        self.approx_value = 0
        self.error_value = 0
        self.seed = seed
        self.setup_logging()

    def integrate(self, n):
        """
        Perform the Monte-Carlo to approximate the integral of the function.
        """
        if self.seed is not None:
            np.random.seed(self.seed)
        h = (self.b-self.a)/n
        res = 0
        for i in range(0, n):
            x = np.random.uniform(self.a, self.b)
            # x = np.random.rand()*(self.b-self.a)+self.a
            res += self.f(x)
        self.approx_value = h*res
        return self.approx_value

    def error(self, n):
        """
        Calculate the error between the approximation and the exact value.
        """
        approx = self.integrate(n)
        self.error_value = abs(approx - self.exact)
        return abs(approx - self.exact)

    def find_degree(self, tol):
        """
        Find the degree needed to achieve a certain tolerance.
        """
        n = 1
        while self.error(n) > tol and n < self.max_iter:
            n += 1
        return n

    def print_results(self, n):
        """
        Print the degree, approximation, and error.
        """
        self.logger.info("Degree: {}".format(n))
        self.logger.info("Approximation: {}".format(self.approx_value))
        self.logger.info("Error: {}".format(self.error_value))

    def setup_logging(self):
        logging.basicConfig(filename='monte_carlo.log',
                            format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', datefmt='%Y-%m-%d:%H:%M:%S', level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)


if __name__ == '__main__':
    def f(x): return x*x
    monte_carlo = MonteCarlo(f, 0.0, 1.0, 1.0/3)
    degree = monte_carlo.find_degree(1e-3)
    monte_carlo.print_results(degree)
