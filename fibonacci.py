"""
A module to calculate and evaluate the Fibonacci sequence on
its recursive attribute.
"""


from numbers import Number


class Fibonacci:
    """
    Provides methods to calculate and evaluate the
    Fibonacci sequence.
    """

    def fibonacci(self, _n: int) -> int:
        """Calculates the fibonacci sequence based on n

        _n -- the end of sequence
        Return: the last computed number of the sequence
        """
        if _n in (0, 1):
            return _n
        _a, _b = 0, 1
        for _ in range(_n - 1):
            _a, _b = _b, _a + _b
        return _b

    def golden_ratio_approx(self, _n: int):
        """Computes the approximation of the golden ratio for a
        fibonacci sequence and a fibonacci sequence + 1

        _n -- the end of sequence
        Return: the approximation
        """

        f_n = self.fibonacci(_n)
        f_n_plus_1 = self.fibonacci(_n + 1)
        phi_approx = f_n_plus_1 / f_n
        return phi_approx

    def find_relative_error(self, lookup: Number) -> int:
        """Find the first fibonacci number where the relative error
        is smaller than a given lookup.

        lookup -- a value for which the relative error should be smaller
        Return: The first number
        """
        _n = 2
        while True:
            phi_approx_n = self.golden_ratio_approx(_n)
            relative_error_n = abs(phi_approx_n - (1 + 5**0.5) / 2) / (
                (1 + 5**0.5) / 2
            )
            if relative_error_n < lookup:
                break
            _n += 1
        return _n
