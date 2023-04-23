"""
This module provides functions to find the n for an
approximation on a limit.
"""
import math


class NSequence:
    """
    Provides methods to calculate sequences on a given n.
    Also evaluates the approximation on the limit of each function.
    """

    def f_1(self, _n) -> float:
        """
        Calculates a sequence on n. f_n = (2/3)^n\n
        Parameters:
        n (int or float): n
        """
        _numerator = 2
        _denominator = 3
        return math.pow(_numerator / _denominator, _n)

    def f_2(self, _n) -> float:
        """
        Calculates a sequence on n. f_n = (n³/2^n)\n
        Parameters:
        n (int or float): n
        """
        _numerator = math.pow(_n, 3)
        _denominator = math.pow(2, _n)
        return _numerator / _denominator

    def f_3(self, _n) -> float:
        """
        Calculates a sequence on n. f_n = (n+1/n)^n\n
        Parameters:
        n (int or float): n
        """
        _numerator = _n + 1
        _denominator = _n
        return math.pow(_numerator / _denominator, _n)

    def f_4(self, _n) -> float:
        """
        Calculates a sequence on n. f_n = (1+(5/n))^n\n
        Parameters:
        n (int or float): n
        """
        _numerator = 5
        _denomnitator = _n
        return math.pow(1 + (_numerator / _denomnitator), _n)
