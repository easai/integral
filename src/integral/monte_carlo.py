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

    def get_var(self, a, b, m):
        fx = []
        for i in range(0, m):
            x = np.random.uniform(a, b)
            fx.append(self.f(x))
        return np.var(fx)

    def get_ratio(self, a, b, m):
        res = 1.0
        if a < b:
            mid = (b-a)/2.0
            var_a = self.get_var(a, mid, m)
            var_b = self.get_var(mid, b, m)
        return math.sqrt(var_a/var_b)

    def integrate(self, n):
        m = 100
        r = self.get_ratio(self.a, self.b, m)
        n_a = math.ceil(1/(1+r)*n)
        n_b = n-n_a
        mid = (self.b-self.a)/2
        res = 0
        if 0 < n_a:
            res += self._integrate(self.a, mid, n_a)
        if 0 < n_b:
            res += self._integrate(mid, self.b, n_b)
        return res

    def integrate_non_adaptive(self, n):
        return self._integrate(self.a, self.b, n)      

    def _integrate(self, a, b, n):
        """
        Perform the Monte-Carlo to approximate the integral of the function.
        """
        if self.seed is not None:
            np.random.seed(self.seed)
        h = (b-a)/n
        res = 0
        for i in range(0, n):
            x = np.random.uniform(self.a, self.b)
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
        if self.error_value <= tol:
            logging.info('Tolerance achieved')
        else:
            logging.warning('Tolerance not achieved')
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
