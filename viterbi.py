import numpy as np
import math

transition = np.array([
     #S0    #S1    #S2    #S3      #S4     #S5
    [0.95,  0.05,   0,      0,      0,      0],  # InterGen(S0)
    [0,     0,      1,      0,      0,      0],  # A(S1)
    [0,     0,      0,      1,      0,      0],  # Codon1(S2)
    [0,     0,      0,      0,      1,      0],  # Codon2(S3)
    [0,     0,      0.8,    0,      0,      0.2],  # Codon3(S4)
    [0.95,  0.05,   0,      0,      0,      0]  # T(S5)
])

emission = np.array([
    #A      #C      #T      #G
    [0.3,   0.2,    0.3,    0.2],  # InterGen(S0)
    [1.0,   0.0,    0.0,    0.0],  # A(S1)
    [0.0,   0.4,    0.2,    0.4],  # Codon1(S2)
    [0.0,   0.4,    0.2,    0.4],  # Codon2(S3)
    [0.0,   0.4,    0.2,    0.4],  # Codon3(S4)
    [0.0,   0.0,    1.0,    0.0]  # T(S5)
])


States = {
    "InterGen(S0)": 0,
    "A(S1)":        1,
    "Codon1(S2)":   2,
    "Codon2(S3)":   3,
    "Codon3(S4)":   4,
    "T(S5)":        5
}

Letters = {
    "A": 0,
    "C": 1,
    "T": 2,
    "G": 3
}



"""
emission = np.array([
    [{"A": 0.3}, {"C": 0.2}, {"T": 0.3}, {"G": 0.2}],  # InterGen (S0)
    [{"A": 1}, {"C": 0}, {"T": 0}, {"G": 0}],  # A        (S1)
    [{"A": 0}, {"C": 0.4}, {"T": 0.2}, {"G": 0.4}],  # Codon1   (S2)
    [{"A": 0}, {"C": 0.4}, {"T": 0.2}, {"G": 0.4}],  # Codon2   (S3)
    [{"A": 0}, {"C": 0.4}, {"T": 0.2}, {"G": 0.4}],  # Codon3   (S4)
    [{"A": 0}, {"C": 0}, {"T": 1}, {"G": 0}]  # T        (S5)
])"""
sequence = "CCATCGCACTCCGATGTGGCCGGTGCTCACGTTGCCT"


def viterbi(s, transitions, emissions):
    s_length = len(s)  # n.Rows
    num_of_states = len(emissions)  # k.Columns

    v = np.zeros((num_of_states, s_length), dtype=object)
    v[0, 0] = (math.log(1), -1) #the tuple is to know from what i value in the previous column the maximum was chosen.
    # initialize v[0, j]
    for i in range(1, num_of_states):
        v[i, 0] = (math.log(emission[States["InterGen(S0)"], Letters[s[0]]]), -1) #there is no previous because this is the most left column.

    for j in range(0, num_of_states):
        for i in range(1, len(s)):
            for l in range(0, num_of_states):
                v[j,i] = math.log(emission[l, i]) + max([v[l,i-1] + transition[l,j]])
    print(v)

viterbi(sequence, transition, emission)