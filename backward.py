import numpy as np
import math
import sys
from constants import sequence, transition_matrix, emission_matrix, states, letters


def backward(s, transitions, emissions):
    s_length = len(s)  # n.Rows
    num_of_states = len(emissions)  # k.Columns

    b = np.zeros((num_of_states, s_length), dtype=float)

    # initialize b[n, i]
    for i in range(0, num_of_states):
        b[i, len(s) - 1] = 1 # The most left column

    for i in reversed(range(0, len(s) - 1)):
        X_i = letters[s[i + 1]] # Because of backward, we want the X_i+1
        for j in range(0, num_of_states):
            for l in range(0, num_of_states):
                transition = transitions[l, j]
                emission = emissions[l, X_i]  #emission inserted into the "l" for because he is being dependent on l

                b[j, i] += b[l, i + 1] * transition * emission

    return(b)


#print(backward(sequence, transition_matrix, emission_matrix))




