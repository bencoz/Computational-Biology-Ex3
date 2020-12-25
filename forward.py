import numpy as np
import math
import sys
from constants import sequence, transition_matrix, emission_matrix


def forward(s, transitions, emissions):
    s_length = len(s)  # n.Rows
    num_of_states = len(emissions)  # k.Columns

    f = np.zeros((num_of_states, s_length), dtype=float)

    # initialize f[0, i]
    f[0, 0] = 1
    for i in range(1, num_of_states):
        f[i, 0] = 0

    for i in range(1, len(s)):
        for j in range(0, num_of_states):
            emission = emissions[j].get(s[i])
            if emission == 0.0:
                log_emit = -math.inf
            else:
                log_emit = math.log(emission)
            a_max = sys.float_info.min
            a_l = []
            for l in range(0, num_of_states):
                if transitions[l, j] == 0.0:
                    log_trans = -math.inf
                else:
                    log_trans = math.log(transitions[l, j])

                curr = f[l, i - 1] + log_trans
                if curr > a_max:
                    a_max = curr
                a_l.append(curr)

                # Regular
                # f[j, i] += f[l, i - 1] * transitions[l, j] * emission

            f[j, i] = 0
            for l in range(0, num_of_states):
                b_l = a_l[l] - a_max
                f[j, i] += math.exp(b_l)

            if f[j, i] == 0.0:
                log_f = -math.inf
            else:
                log_f = math.log(f[j, i])
            f[j, i] = log_f + a_max + log_emit

    likelihood = 0
    for i in range(0, num_of_states):
        curr = f[i, len(s) - 1]
        if curr > -math.inf:
            likelihood += curr
    print(f"forward likelihood is: {likelihood}")
    return f


forward(sequence, transition_matrix, emission_matrix)
