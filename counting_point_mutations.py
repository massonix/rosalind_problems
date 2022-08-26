"""
Evolution as a Sequence of Mistakesclick to expand
Problem

Figure 2. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
Sample Output
7
"""


sequence1 = input()
sequence2 = input()


hamming_distance = 0
for a, b in zip(sequence1, sequence2):
    if a != b:
        hamming_distance += 1
        
print(hamming_distance)
