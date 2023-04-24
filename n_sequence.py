"""
This module provides functions to find the n for an
approximation on a limit.
"""
import cmath
import math
import os

import matplotlib.pyplot as plt
import numpy as np
from numpy import mat, void


class NSequence:
    """
    Provides methods to calculate sequences on a given n.
    Also evaluates the approximation on the limit of each function.
    """

    current_file = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file)
    out_folder = "out/n_sequence/"

    f_1_string_tex = r"$f(n) = (\frac {2} {3})^n$"
    f_2_string_tex = r"$f(n) = (\frac {n³} {2^n})$"
    f_3_string_tex = r"$f(n) = (\frac {n+1} {n})^n$"
    f_4_string_tex = r"$f(n) = (1 + \frac {5} {n})^n $"

    f_1_string = "f_1"
    f_2_string = "f_2"
    f_3_string = "f_3"
    f_4_string = "f_4"

    @staticmethod
    def safely_divide(_numerator: float, _denominator: float):
        """
        Devides a given numerator by a given denominator and catches error cases.
        """
        result = None
        try:
            result = _numerator / _denominator
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            result = 0

        return result

    def power(self, base, exponent) -> float:
        """
        Calculates the power of a given base by a given exponent.
        Useful for negative exponents.
        """
        if exponent >= 0:
            return math.pow(base, exponent)

        denominator = math.pow(base, abs(exponent))
        return self.safely_divide(1, denominator)

    def f_1(self, _n) -> float:
        """
        Calculates a sequence on n. f_n = (2/3)^n\n
        Parameters:
        n (int or float): n
        """
        _numerator = 2
        _denominator = 3
        _base = self.safely_divide(_numerator, _denominator)
        return self.power(_base, _n)

    def f_2(self, _n) -> float:
        """
        Calculates a sequence on n. f_n = (n³/2^n)\n
        Parameters:
        n (int or float): n
        """
        _numerator = self.power(_n, 3)
        _denominator = self.power(2, _n)
        return self.safely_divide(_numerator, _denominator)

    def f_3(self, _n) -> float:
        """
        Calculates a sequence on n. f_n = (n+1/n)^n\n
        Parameters:
        n (int or float): n
        """
        _numerator = _n + 1
        _denominator = _n
        _base = self.safely_divide(_numerator, _denominator)
        return self.power(_base, _n)

    def f_4(self, _n) -> float:
        """
        Calculates a sequence on n. f_n = (1+5/n)^n\n
        Parameters:
        n (int or float): n
        """
        _numerator = 5
        _denominator = _n
        _base = self.safely_divide(_numerator, _denominator)
        return self.power(1 + _base, _n)

    fn_to_string_dict = {
        "f_1": f_1_string,
        "f_2": f_2_string,
        "f_3": f_3_string,
        "f_4": f_4_string,
    }
    latex_dict = {
        "f_1": f_1_string_tex,
        "f_2": f_2_string_tex,
        "f_3": f_3_string_tex,
        "f_4": f_4_string_tex,
    }

    def plot_function(
        self, _function_name: str, x_min: int, x_max: int, num_points=1000
    ) -> void:
        """
        Plots a given function on a given range of x_min and x_max and
        saves the png in a directory.
        """
        _function = getattr(self, _function_name)
        x_values = np.linspace(x_min, x_max, num_points)
        y_values = [_function(_n) for _n in x_values]

        plt.plot(x_values, y_values)
        plt.xlabel(r"$n$")
        plt.ylabel(r"$f(n)$")
        plt.title(self.latex_dict[_function_name])
        plt.savefig(
            os.path.join(
                self.current_dir,
                self.out_folder,
                self.fn_to_string_dict[_function_name],
            )
        )
        plt.show()
