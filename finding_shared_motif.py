"""
Problem
A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Sample Dataset
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
Sample Output
AC
"""

import numpy as np
fasta = open("example_fasta.fa", "r")
fasta_lines = fasta.readlines()
string_list = []
for line in fasta_lines:
    if line.startswith(">"):
        string_list.append("")
    else:
        string_list[-1] += line.strip("\n")
        
        
longest_substring = ""
substring_len = 1
count = 1
substrings_set = set()
while True:
    for i in range(len(string_list[0])):
        substring = string_list[0][i:(i+substring_len)]
        if len(substring) == substring_len:
            substrings_set.add(substring)
    for substring in list(substrings_set):
        tmp = np.array([substring in x for x in string_list[1:]])
        if np.sum(tmp) == len(string_list[1:]):
            longest_substring = substring
            break
    if len(longest_substring) < substring_len:
        break
    substrings_set = set()
    substring_len +=1
    
print(longest_substring)
