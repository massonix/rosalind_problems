"""
Problem
A subsequence of a string is a collection of symbols contained in order (though not necessarily contiguously) in the string (e.g., ACG is a subsequence of TATGCTAAGATC). The indices of a subsequence are the positions in the string at which the symbols of the subsequence appear; thus, the indices of ACG in TATGCTAAGATC can be represented by (2, 5, 9).

As a substring can have multiple locations, a subsequence can have multiple collections of indices, and the same index can be reused in more than one appearance of the subsequence; for example, ACG is a subsequence of AACCGGTT in 8 different ways.

Given: Two DNA strings s
 and t
 (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s
 in which the symbols of t
 appear as a subsequence of s
. If multiple solutions exist, you may return any one.

Sample Dataset
>Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA
Sample Output
3 8 10
"""

# Read data
seqs = []
with open("tmp/rosalind_sseq.txt", "r") as f:
	lines = f.readlines()
	del lines[0]
	seq = ""
	for line in lines:
		if line.startswith(">"):
			seqs.append(seq)
			seq = ""
		else:
			seq += line.rstrip("\n")
	seqs.append(seq)
s, t = seqs


# Get all indices of each symbol in string s
indices = {"A":[], "C":[], "G":[], "T":[]}
for index, base in enumerate(s):
	indices[base].append(index)


# Get indices of s in which the symbols oof t appear as a subsequence of s
current_max_index = -1
output_indices = []
for base in t:
	for index in indices[base]:
		if index > current_max_index:
			output_indices.append(index+1)
			current_max_index = index
			break

# Print result
output_indices = [str(x) for x in output_indices]
output_indices = " ".join(output_indices)
print(output_indices)







