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

    # print the log likelihood for the entire sequence (log(P(X|HMM)))
    likelihood = 0
    a_max = -math.inf
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

    # print for each position the state and its posterior conditional probability
    posterior_probability = np.zeros([num_of_states, len(s)])
    posterior_conditional_probability = np.zeros([num_of_states, len(s)])
    for i in range(0, len(s)):
        for j in range(0, num_of_states):
            posterior_probability[j, i] = F[j, i] + B[j, i]  # Because log of product is the sum

    print("Base\t|\tState\t|\tProb")
    for i in range(0, len(s)):
        max = -math.inf
        state = -1
        for j in range(0, num_of_states):
            curr = posterior_probability[j, i] - likelihood # Because log of division is the difference
            if curr > max:
                max = curr
                state = j
            posterior_conditional_probability[j, i] = curr
        print(f"{s[i]}\t\t|\t{state}\t\t|\t{max}")



    # for each position i along the sequence the HMM state s
    # with highest posterior probability for that position: P(Si=s|X,HMM).
    highest_posterior_probability = np.zeros(len(s))
    for i in range(0, len(s)):
        max = -math.inf
        state = -1
        for j in range(0, num_of_states):
            curr = F[j, i] + B[j, i]  # Logs
            if curr > max:
                state = j
                max = curr
        highest_posterior_probability[i] = state + 1

    return highest_posterior_probability


print(posterior_decoding(sequence, transition_matrix, emission_matrix))
