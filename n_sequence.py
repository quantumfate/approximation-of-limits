"""
This module provides functions to find the n for an
approximation on a limit.
"""
import math
import os
from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
from numpy import void


class NSequence:
    """
    Provides methods to calculate sequences on a given n.
    Also evaluates the approximation on the limit of each function.
    """

    current_file = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file)
    out_folder = "/out/n_sequence/"

    f_1_string_tex = r"$f(n) = (\frac {2} {3})^n$"
    f_2_string_tex = r"$f(n) = (\frac {n³} {2^n})$"
    f_3_string_tex = r"$f(n) = (\frac {n+1} {n})^n$"
    f_4_string_tex = r"$f(n) = (1 + \frac {5} {n})^n $"

    f_1_string = "f_1"
    f_2_string = "f_2"
    f_3_string = "f_3"
    f_4_string = "f_4"

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

    fn_to_string_dict = {
        f_1: f_1_string,
        f_2: f_2_string,
        f_3: f_3_string,
        f_4: f_4_string,
    }
    latex_dict = {
        f_1: f_1_string_tex,
        f_2: f_2_string_tex,
        f_3: f_3_string_tex,
        f_4: f_4_string_tex,
    }

    def plot_function(
        self, _function: Callable, x_min: int, x_max: int, num_points=1000
    ) -> void:
        """
        Plots a given function on a given range of x_min and x_max and
        saves the png in a directory.
        """
        x_values = np.arange(x_min, x_max, num_points)
        y_values = [_function(_n) for _n in x_values]

        plt.plot(x_values, y_values)
        plt.xlabel(r"$n$")
        plt.ylabel(r"$f(n)$")
        plt.title(self.latex_dict[_function])
        plt.savefig(
            self.current_dir + self.out_folder + self.fn_to_string_dict[_function]
        )
        plt.show()
