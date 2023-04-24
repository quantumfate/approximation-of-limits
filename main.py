"""
Runs n sequence and fibonacci modules.
"""
from fibonacci import Fibonacci
from n_sequence import NSequence

# N sequence
n_seq = NSequence()
n_seq.plot_function("f_1", -100, 160)
n_seq.plot_function("f_2", -100, 160)
n_seq.plot_function("f_3", -100, 160)
n_seq.plot_function("f_4", -100, 260)

# fibonacci
fib_seq = Fibonacci()
N_PERCENT = fib_seq.find_relative_error(0.01)
N_PERMILLE = fib_seq.find_relative_error(0.001)
print(
    "The first two Fibonacci numbers with relative error less than 1% are:",
    N_PERCENT,
    N_PERCENT + 1,
)
print(
    "The first two Fibonacci numbers with relative error less than 1 permille are:",
    N_PERMILLE,
    N_PERMILLE + 1,
)
