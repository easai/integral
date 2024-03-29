import math
import scipy
import logging

class GaussJacobiQuadrature:
    """
    A class to perform Gauss-Jacobi quadrature.
    """
    def __init__(self, f, alpha, beta, exact=None):
        """
        Initialize the class with the function to integrate.
        """
        self.f = f
        self.exact = exact
        self.alpha = alpha
        self.beta = beta
        self.approx_value = 0
        self.error_value = 0
        self.setup_logging()

    def jacobi_nodes_and_weights(self, n):
        """
        Generate nodes and weights for the Gauss-Jacobi quadrature of order n.
        """
        x,w = scipy.special.roots_jacobi(n, self.alpha, self.beta)
        return x, w

    def integrate(self, n):
        """
        Perform the Gauss-Jacobi quadrature to approximate the integral of the function.
        """
        x, w = self.jacobi_nodes_and_weights(n)
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
        if self.error_value <= tol:
            self.logger.info('Tolerance achieved')
        else:
            self.logger.warning('Tolerance not achieved')
        return n

    def print_results(self, n):
        """
        Print the degree, approximation, and error.
        """
        self.logger.info("Degree: {}".format(n))
        self.logger.info("Approximation: {}".format(self.approx_value))
        self.logger.info("Error: {}".format(self.error_value))
    
    def print_msg(self, msg):
        self.logger.info(msg)

    def print_nodes_and_weights(self, n):
        x, w = self.jacobi_nodes_and_weights(n)
        self.logger.info(f"Abscissas: {x=}")
        self.logger.info(f"Weights: {w=}")

    def setup_logging(self):
        logging.basicConfig(filename='gauss_jacobi_quadrature.log',
                            format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', datefmt='%Y-%m-%d:%H:%M:%S', level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)



# Example usage
f = lambda x: x*x
g = GaussJacobiQuadrature(f, 1,1, 4.0/15.0)
g.print_msg("f(x)=x^2")
degree = g.find_degree(1e-6)
g.print_results(degree)

