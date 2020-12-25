import numpy as np
import math
import sys
from constants import sequence, transition_matrix, emission_matrix
from utils import mylog


def backward(s, transitions, emissions):
    s_length = len(s)  # n.Rows
    num_of_states = len(emissions)  # k.Columns

    b = np.zeros((num_of_states, s_length), dtype=float)

    # initialize b[n, i]
    for i in range(0, num_of_states):
        b[i, len(s) - 1] = math.log(1)  # The most left column

    for i in reversed(range(0, len(s) - 1)):
        for j in range(0, num_of_states):
            a_max = sys.float_info.min
            a_l = []
            for l in range(0, num_of_states):
                emission = emissions[l].get(s[i + 1])  # emission inserted into the "l" for because he is being dependent on l

                curr = b[l, i + 1] + mylog(transitions[j, l]) + mylog(emission)
                if curr > a_max:
                    a_max = curr
                a_l.append(curr)

                # Regular
                # b[j, i] += b[l, i + 1] * transition * emission

            b[j, i] = 0
            for l in range(0, num_of_states):
                b_l = a_l[l] - a_max
                b[j, i] += math.exp(b_l)

            b[j, i] = mylog(b[j, i]) + a_max

    return b


backward(sequence, transition_matrix, emission_matrix)
