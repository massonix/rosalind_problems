"""
Problem
For DNA strings s1
 and s2
 having the same length, their transition/transversion ratio R(s1,s2)
 is the ratio of the total number of transitions to the total number of transversions, where symbol substitutions are inferred from mismatched corresponding symbols as when calculating Hamming distance (see “Counting Point Mutations”).

Given: Two DNA strings s1
 and s2
 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2)
.

Sample Dataset
>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT
Sample Output
1.21428571429
"""


# Parse fasta file
fasta_file = open("tmp/rosalind_tran.txt", "r")
lines = fasta_file.readlines()
sequences = []
seq = ""
for line in lines:
    if line.startswith(">"):
        sequences.append(seq)
        seq = ""
    else:
        seq += line.strip("\n")
sequences.append(seq)
sequences = sequences[1:]


# Calculate transition / transversion ratio
transitions = ["AG", "GA", "CT", "TC"]
transversions = ["AC", "CA", "AT", "TA", "GC", "CG", "GT", "TG"]
counts = {"transitions":0, "transversions":0}
for nt1, nt2 in zip(sequences[0], sequences[1]):
    if (nt1+nt2) in transitions:
        counts["transitions"] += 1
    elif (nt1+nt2) in transversions:
        counts["transversions"] += 1

print(counts["transitions"] / counts["transversions"])