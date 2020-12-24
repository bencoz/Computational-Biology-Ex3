import numpy as np
import math
from constants import sequence, transition_matrix, emission_matrix, states, letters


def forward(s, transitions, emissions):
    s_length = len(s)  # n.Rows
    num_of_states = len(emissions)  # k.Columns

    f = np.zeros((num_of_states, s_length), dtype=float)

    # initialize f[0, i]
    f[0, 0] = 1
    for i in range(1, num_of_states):
        f[i, 0] = 0

    for i in range(1, len(s)):
        X_i = letters[s[i]]
        for j in range(0, num_of_states):
            emission = emissions[j, X_i]
            for l in range(0, num_of_states):
                # Regular
                f[j, i] += f[l, i - 1] * transitions[l, j] * emission
    print(f)


forward(sequence, transition_matrix, emission_matrix)