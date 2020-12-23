import numpy as np
import math
import sys
from constants import sequence, transition_matrix, emission_matrix, states, letters


def viterbi(s, transitions, emissions):
    s_length = len(s)  # n.Rows
    num_of_states = len(emissions)  # k.Columns

    v = np.zeros((num_of_states, s_length), dtype=object)
    v[0, 0] = (math.log(1), -1)  # the tuple is to know from what i value in the previous column the maximum was chosen.
    # initialize v[0, j]
    for i in range(1, num_of_states):
        v[i, 0] = (math.log(emissions[states["InterGen(S0)"], letters[s[0]]]), -1)  # there is no previous because this is the most left column.

    for i in range(1, len(s)):

        X_i = letters[s[i]]
        for j in range(0, num_of_states):

            curr_max = float('-inf')
            max_prev_state_index = -1
            emit = emissions[j, X_i]
            if emit == 0.0:
                emit = sys.float_info.epsilon
            for l in range(0, num_of_states):
                trans = transitions[l, j]
                if trans == 0.0:
                    trans = sys.float_info.epsilon
                score = math.log(emit) + float(v[l, i - 1][0]) + math.log(trans)

                if score > curr_max:
                    curr_max = score
                    max_prev_state_index = l
            v[j, i] = (curr_max, max_prev_state_index)
    print(v)


viterbi(sequence, transition_matrix, emission_matrix)
