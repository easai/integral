"""Use the left Riemann Rule to approximate integral

"""
from math import *


class IntegralRiemann():
    def __init__(self):
        """Constructor.

        Args:
        f(function): the function
        """
        pass

    def left_riemann(self, f, start, end, n):
        """Calculate left Riemann sum.

        Approximate integral of f on the interval [start,end] over n subintervals
        using the left Riemann rule

        Args:
            start (int): the start index
            end (int): the end index
            n (int): the number of intervals
        """
        deltax = (end - start) / n
        domain = [start + x * deltax for x in range(0, n)]
        value = [f(x) for x in domain]
        res = deltax * sum(value)
        return res

    def right_riemann(self, f, start, end, n):
        """Calculate right Riemann sum.

        Approximate integral of f on the interval [start,end] over n subintervals
        using the right Riemann rule

        Args:
            start (int): the start index
            end (int): the end index
            n (int): the number of intervals
        """
        deltax = (end - start) / n
        domain = [start + x * deltax for x in range(1, n + 1)]
        value = [f(x) for x in domain]
        res = deltax * sum(value)
        return res

    def left_riemann_n(self, f, a, b, n, limit):
        """ Obtain the minimum number of subintervals n with the error under limit using the left Riemann rule
        """
        deltax = (b - a) / n
        domain = [a + x * deltax for x in range(0, n + 1)]
        value = [f(x) for x in domain]
        maxff = max(value)
        return ceil(sqrt(maxff * (b - a)**3 / (24 * limit)))

    def left_riemann_err(self, f, a, b, n):
        """ Calculate the max error guaranteed by the left Riemann Rule
        """
        deltax = (b - a) / n
        domain = [a + x * deltax for x in range(0, n + 1)]
        value = [f(x) for x in domain]
        maxff = max(value)
        return maxff * (b - a)**3 / (24 * n**2)
