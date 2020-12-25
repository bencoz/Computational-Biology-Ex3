import numpy as np
import math
import sys
from constants import sequence, transition_matrix, emission_matrix


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
                transition = transitions[l, j]
                if transition == 0.0:
                    log_trans = -math.inf
                else:
                    log_trans = math.log(transitions[l, j])
                emission = emissions[l].get(
                    s[i + 1])  # emission inserted into the "l" for because he is being dependent on l
                if emission == 0.0:
                    log_emit = -math.inf
                else:
                    log_emit = math.log(emission)

                curr = b[l, i + 1] + log_trans + log_emit
                if curr > a_max:
                    a_max = curr
                a_l.append(curr)

                # Regular
                # b[j, i] += b[l, i + 1] * transition * emission

            b[j, i] = 0
            for l in range(0, num_of_states):
                b_l = a_l[l] - a_max
                b[j, i] += math.exp(b_l)

            if b[j, i] == 0.0:
                log_f = -math.inf
            else:
                log_f = math.log(b[j, i])
            b[j, i] = log_f + a_max

    return (b)


print(backward(sequence, transition_matrix, emission_matrix))
