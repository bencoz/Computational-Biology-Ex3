import numpy as np

transition_matrix = np.array([
    # S0    #S1    #S2    #S3      #S4     #S5
    [0.95, 0.05, 0.0, 0.0, 0.0, 0.0],  # InterGen(S0)
    [0.0, 0.0, 1.0, 0.0, 0.0, 0.0],  # A(S1)
    [0.0, 0.0, 0.0, 1.0, 0.0, 0.0],  # Codon1(S2)
    [0.0, 0.0, 0.0, 0.0, 1.0, 0.0],  # Codon2(S3)
    [0.0, 0.0, 0.8, 0.0, 0.0, 0.2],  # Codon3(S4)
    [0.95, 0.05, 0.0, 0.0, 0.0, 0.0]  # T(S5)
])

emission_matrix = np.array([
    # A      #C      #T      #G
    [0.3, 0.2, 0.3, 0.2],  # InterGen(S0)
    [1.0, 0.0, 0.0, 0.0],  # A(S1)
    [0.0, 0.4, 0.2, 0.4],  # Codon1(S2)
    [0.0, 0.4, 0.2, 0.4],  # Codon2(S3)
    [0.0, 0.4, 0.2, 0.4],  # Codon3(S4)
    [0.0, 0.0, 1.0, 0.0]  # T(S5)
])

states = {
    "InterGen(S0)": 0,
    "A(S1)": 1,
    "Codon1(S2)": 2,
    "Codon2(S3)": 3,
    "Codon3(S4)": 4,
    "T(S5)": 5
}

letters = {
    "A": 0,
    "C": 1,
    "T": 2,
    "G": 3
}

sequence = "CCATCGCACTCCGATGTGGCCGGTGCTCACGTTGCCT"
