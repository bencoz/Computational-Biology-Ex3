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
        v[i, 0] = (math.log(emissions[states["InterGen(S0)"], letters[s[0]]]),
                   -1)  # there is no previous because this is the most left column.

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

    last_cloumn_max = float("-inf")
    probabilities_of_sequence = []
    most_probable_sequence_of_states = []

    for idx in range(num_of_states):
        if (v[idx, len(s) - 1][0] > last_cloumn_max):
            last_cloumn_max = v[idx, len(s) - 1][0]
            prev_index = v[idx, len(s) - 1][1]
            prev_probability = "{:.2f}".format(v[idx, len(s) - 1][0])
            most_probable_sequence_of_states.append(str(idx + 1))
            probabilities_of_sequence.append(prev_probability)

    for k in reversed(range(1, len(s))):
        most_probable_sequence_of_states.append(str(prev_index + 1))
        probabilities_of_sequence.append(prev_probability)
        prev_index = v[prev_index, k - 1][1]
        prev_probability = v[prev_index, k - 1][0]
        # prev_probability = "{:.2f}".format(v[prev_index,k-1][0])  # only 2 digit after the dot

    probabilities_of_sequence.reverse()
    most_probable_sequence_of_states.reverse()

    return most_probable_sequence_of_states, probabilities_of_sequence


sequence_of_probabilities, sequence_of_states = viterbi(sequence, transition_matrix, emission_matrix)

for index in range(len(sequence)):
    print(sequence_of_probabilities[index], "\t|\t", sequence_of_states[index])
