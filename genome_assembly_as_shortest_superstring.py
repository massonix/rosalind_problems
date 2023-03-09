"""
Problem
For a collection of strings, a larger string containing every one of the smaller strings as a substring is called a superstring.

By the assumption of parsimony, a shortest possible superstring over a collection of reads serves as a candidate chromosome.

Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).

Sample Dataset
>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC
Sample Output
ATTAGACCTGCCGGAATAC
"""

# Read fasta file and create a list of DNA sequences
fasta_file = open("tmp/rosalind_long.txt", "r")
lines = fasta_file.readlines()
sequences = []
seq = ""
for line in lines:
    if line.startswith(">"):
        sequences.append(seq)
        seq= ""
    else:
        seq += line.strip("\n")
sequences.append(seq)
sequences = sequences[1:]


# Define a function that generates shortest superstring given two strings
def find_shortest_superstring(long_string, short_string):
    """
    Find shortest superstring from 2 DNA sequences

    :param long_string: first DNA string
    :param short_string: second DNA string
    :return: A list with 2 elements, 1. shortest superstring (empty if it does not exist), 2. largest common substring
    """
    min_length = min([len(long_string), len(short_string)])
    substring1 = ""
    substring2 = ""

    # Append short string to the end of the long string
    for i in range(min_length):
        if long_string[:(i+1)] == short_string[(-i-1):]:
            substring1 = long_string[:(i+1)]
            superstring1 = short_string + long_string.replace(substring1, "")

    # Append long string to the end of short string
    for i in range(min_length):
        if short_string[:(i+1)] == long_string[(-i-1):]:
            substring2 = short_string[:(i+1)]
            superstring2 = long_string + short_string.replace(substring2, "")

    # Return
    if len(substring1) > (len(short_string) / 2):
        return superstring1
    elif len(substring2) > (len(short_string) / 2):
        return superstring2
    else:
        return ""


# Find shortest superstring iterating by comparing all vs all sequences
superstring = sequences[0]
sequences.pop(0)
while len(sequences) > 0:
    for i, seq in enumerate(sequences):
        tmp_string = find_shortest_superstring(long_string=superstring, short_string=seq)
        if len(tmp_string) > 0:
            superstring = tmp_string
            sequences.pop(i)
            break
print(superstring)

