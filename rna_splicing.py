"""
Problem
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

Sample Dataset
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
Sample Output
MVYIADKQHVASREAYGHMFKVCA
"""


codon_dict = {"UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V",
"UUC":"F", "CUC":"L", "AUC":"I", "GUC":"V",
"UUA":"L", "CUA":"L", "AUA":"I", "GUA":"V",
"UUG":"L", "CUG":"L", "AUG":"M", "GUG":"V",
"UCU":"S", "CCU":"P", "ACU":"T", "GCU":"A",
"UCC":"S", "CCC":"P", "ACC":"T", "GCC":"A",
"UCA":"S", "CCA":"P", "ACA":"T", "GCA":"A",
"UCG":"S", "CCG":"P", "ACG":"T", "GCG":"A",
"UAU":"Y", "CAU":"H", "AAU":"N", "GAU":"D",
"UAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D",
"UAA":"Stop","CAA":"Q", "AAA":"K", "GAA":"E",
"UAG":"Stop", "CAG":"Q", "AAG":"K", "GAG":"E",
"UGU":"C", "CGU":"R", "AGU":"S", "GGU":"G",
"UGC":"C", "CGC":"R", "AGC":"S", "GGC":"G",
"UGA":"Stop", "CGA":"R", "AGA":"R", "GGA":"G",
"UGG":"W", "CGG":"R", "AGG":"R", "GGG":"G"}



fasta = open("example_fasta.fa", "r")
lines = fasta.readlines()
fasta.close()

seqs = []
for line in lines:
    if line.startswith(">"):
        seqs.append("")
    else:
        seqs[-1] += line.strip("\n")

     
preRNA = seqs.pop(0)
introns = seqs
RNA = preRNA
for intron in introns:
    index = RNA.find(intron)
    RNA = RNA[:index] + RNA[(index+len(intron)):]

RNA = RNA.replace("T", "U")
protein = ""
init = RNA.find("AUG")
for i in range(init, (len(RNA) - 2), 3):
    codon = RNA[i:(i+3)]
    if codon_dict[codon] == "Stop":
        break
    else:
        protein += codon_dict[codon]

print(protein)

