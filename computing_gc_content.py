"""
Problem
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

Sample Dataset
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
Sample Output
Rosalind_0808
60.919540
"""

fasta = open("example_fasta.fa", "r")
fasta_lines = fasta.readlines()
fasta.close()

strings_list = [""]
gc_dict = {}
current_id = fasta_lines[0].strip(">").strip("\n")
for line in fasta_lines[1:len(fasta_lines)]:
    last_index = len(strings_list) - 1
    if line.startswith(">"):
        gc_count = (strings_list[last_index].count("C") + strings_list[last_index].count("G")) 
        gc_content = gc_count / len(strings_list[last_index]) * 100
        gc_dict[current_id] = gc_content
        strings_list.append("")
        current_id = line.strip(">").strip("\n")
    else:
        strings_list[last_index] += line.strip("\n")

gc_count = (strings_list[last_index].count("C") + strings_list[last_index].count("G")) 
gc_content = gc_count / len(strings_list[last_index]) * 100
gc_dict[current_id] = gc_content
gc_dict_inv = {v: k for k, v in gc_dict.items()}

print(gc_dict_inv[max(gc_dict.values())])
print(max(gc_dict.values()))  




