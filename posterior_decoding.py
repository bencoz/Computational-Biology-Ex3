import numpy as np
import math
import sys

from forward import forward
from backward import backward

from constants import sequence, transition_matrix, emission_matrix


def posterior_decoding(s, transitions, emissions):
    num_of_states = len(emissions)  # k.Columns
    F = forward(s, transitions, emissions)
    B = backward(s, transitions, emissions)

    # Data Likelihood
    likelihood = 0
    a_max = sys.float_info.min
    a_l = []
    for l in range(0, num_of_states):
        curr = F[l, 0] + B[l, 0]
        if curr > a_max:
            a_max = curr
        a_l.append(curr)

    for l in range(0, num_of_states):
        likelihood += math.exp(a_l[l] - a_max)
    likelihood = math.log(likelihood) + a_max
    print(f"Data likelihood is: {likelihood}")


posterior_decoding(sequence, transition_matrix, emission_matrix)
