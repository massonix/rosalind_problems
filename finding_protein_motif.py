"""
Problem
To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.

You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into

http://www.uniprot.org/uniprot/uniprot_id
Alternatively, you can obtain a protein sequence in FASTA format by following

http://www.uniprot.org/uniprot/uniprot_id.fasta
For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

Sample Dataset
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST
Sample Output
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
"""

# Import packages
import urllib.request
import regex

    
# Get UNIPROT ids
file_prot = open("unitprot_ids.txt", "r")
prot_ids = file_prot.readlines()
prot_ids = [x.strip("\n") for x in prot_ids]
prot_id_dic = {x[:6]:x for x in prot_ids}
file_prot.close()


# Get protein sequences
for prot_id in prot_id_dic.keys():
    target_url = "https://rest.uniprot.org/uniprotkb/{}.fasta".format(prot_id)
    url_obj = urllib.request.urlopen(target_url)
    prot_lines = url_obj.readlines()                            
    url_obj.close()
    prot_lines = [x.decode("UTF-8").strip("\n") for x in prot_lines]
    prot_sequence = ""
    for line in prot_lines:
        if not line.startswith(">"):
            prot_sequence += line
    matches = regex.finditer("N[^P][ST][^P]", prot_sequence, overlapped = True)
    indices_motif = [(x.span()[0] + 1) for x in matches]
    if len(indices_motif) > 0:
        print(prot_id_dic[prot_id])
        indices_motif = [str(x) for x in indices_motif]
        print(" ".join(indices_motif))
            


#



