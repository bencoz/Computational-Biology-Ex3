import numpy as np
import math
import sys

from forward import forward
from backward import backward

from constants import sequence, transition_matrix, emission_matrix


def posterior_decoding(s, transitions, emissions):
    F = forward(s, transitions, emissions)
    B = backward(s, transitions, emissions)

    num_of_states = len(emissions)
    sum = 0

    # Checking from slide 28
    for j in range(num_of_states):
        curr = F[j, len(s) - 1]
        if curr > -math.inf:
            sum += math.exp(curr)
    ratio = sum / math.exp(B[0, 0])
    if math.fabs(1 - ratio) < 0.0000000001:
        print("The values are the same")
    print(sum, ", ", B[0, 0])

    """*****************************************************************
    Computation of log-probabilities – with sums - ON FORWARD 
    *****************************************************************"""

    f = np.zeros((num_of_states, len(sequence)), dtype=float)

    f[0, 0] = 1
    for i in range(1, num_of_states):
        f[i, 0] = 0

    for i in range(0, len(sequence)):
        for j in range(1, num_of_states):

            curr_max = float('-inf')
            emit = emissions[j].get(s[i])
            if emit == 0.0:
                emit = sys.float_info.epsilon

            for l in range(0, num_of_states):
                score = F[l, i]

                if score > curr_max:  # Find the maximum
                    curr_max = score
            Sigma = 0

            for l in range(0, num_of_states):
                trans = transitions[l, j]
                if trans == 0.0:
                    trans = sys.float_info.epsilon

                Sigma += math.exp(F[l, i - 1] - curr_max) + math.log(
                    trans)  # Calculate the "Trick"  --> math.exp(F[l, i - 1] - curr_max) == b_l == a_l - a_max
                f[j, i] = math.log(Sigma) + math.log(
                    emit) + curr_max  # a_max + log(Sigma) + log(emission)  --> Slide 35 last line

    print(f)


posterior_decoding(sequence, transition_matrix, emission_matrix)
