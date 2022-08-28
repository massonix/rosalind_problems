"""
Problem
A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.

A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail v and head w is represented by (v,w) (but not by (w,v)). A directed loop is a directed edge of the form (v,v).

For a collection of strings and a positive integer k, the overlap graph for the strings is a directed graph Ok in which each string is represented by a node, and string s is connected to string t with a directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s≠t; we demand s≠t to prevent directed loops in the overlap graph (although directed cycles may be present).

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.s

Sample Dataset
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
Sample Output
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
"""

fasta = open("example_fasta.fa", "r")
fasta_lines = fasta.readlines()
string_dict = {}
for line in fasta_lines:
    if line.startswith(">"):
        current_id = line.strip(">").strip("\n")
        string_dict[current_id] = ""
    else:
        string_dict[current_id] += line.strip("\n")

prefix_dict = {}
suffix_dict = {}
for key in string_dict.keys():
    prefix = string_dict[key][:3]
    suffix = string_dict[key][-3:]
    if prefix not in prefix_dict.keys():
        prefix_dict[prefix] = [key]
    else:
        prefix_dict[prefix].append(key)
    if suffix not in suffix_dict.keys():
        suffix_dict[suffix] = [key]
    else:
        suffix_dict[suffix].append(key)

for key in suffix_dict:
    if key in prefix_dict.keys():
        for id_suffix in suffix_dict[key]:
            for id_prefix in prefix_dict[key]:
                if id_prefix != id_suffix:
                    print(id_suffix, id_prefix)

fasta.close()
