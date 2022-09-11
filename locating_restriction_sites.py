"""
Problem

A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

Sample Dataset
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
Sample Output
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4
"""

fasta = open("rosalind_revp.txt", "r")
lines = fasta.readlines()
fasta.close()
dna = ""
for line in lines:
    if not line.startswith(">"):
        dna += line.strip("\n")


dna_dict = {"A":"T", "C":"G", "G":"C", "T":"A"}
def reverse_complement(string, dna_dict = dna_dict):
    out = "".join([dna_dict[x] for x in string[::-1]])
    return out

count = 4
while count <= 12:
    for i in range(len(dna)-(count-1)):
        substring = dna[i:i+count]
        rev_compl = reverse_complement(substring)
        if substring == rev_compl:
            print(i+1, count)
    count += 1


