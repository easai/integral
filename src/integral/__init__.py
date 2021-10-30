from .riemann import IntegralRiemann as IntegralRiemann
from .midpoint import IntegralMidpoint as IntegralMidpoint
from .simpson import IntegralSimpson as IntegralSimpson
from .trapezoidal import IntegralTrapezoidal as IntegralTrapezoidal

__all__ = ['IntegralRiemann', 'IntegralMidpoint',
           'IntegralSimpson', 'IntegralTrapezoidal']
