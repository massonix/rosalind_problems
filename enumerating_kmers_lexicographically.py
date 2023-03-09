"""
Problem
Assume that an alphabet 𝒜
 has a predetermined order; that is, we write the alphabet as a permutation 𝒜=(a1,a2,…,ak)
, where a1<a2<⋯<ak
. For instance, the English alphabet is organized as (A,B,…,Z)
.

Given two strings s
 and t
 having the same length n
, we say that s
 precedes t
 in the lexicographic order (and write s<Lext
) if the first symbol s[j]
 that doesn't match t[j]
 satisfies sj<tj
 in 𝒜
.

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n
 (n≤10
).

Return: All strings of length n
 that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).

Sample Dataset
A C G T
2
Sample Output
AA
AC
AG
AT
CA
CC
CG
CT
GA
GC
GG
GT
TA
TC
TG
TT
"""

print("Introduce alphabet:")
alphabet = input()
alphabet = alphabet.replace(" ", "")
print("Introduce n:")
n = int(input())
kmers = [[""]]
for i in range(n):
    extended_ks = []
    for ks in kmers[i]:
        tmp = [(ks + x) for x in alphabet]
        extended_ks.extend(tmp)
    kmers.append(extended_ks)

for kmer in kmers[-1]:
    print(kmer)