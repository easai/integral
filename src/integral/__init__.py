from .leftriemann import IntegralLeftRiemann as IntegralLeftRiemann
from .midpoint import IntegralMidpoint as IntegralMidpoint
from .simpson import IntegralSimpson as IntegralSimpson
from .trapezoidal import IntegralTrapezoidal as IntegralTrapezoidal

__all__ = ['IntegralLeftRiemann', 'IntegralMidpoint',
           'IntegralSimpson', 'IntegralTrapezoidal']
