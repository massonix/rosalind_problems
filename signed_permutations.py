"""
Problem
A signed permutation of length n
 is some ordering of the positive integers {1,2,…,n}
 in which each integer is then provided with either a positive or negative sign (for the sake of simplicity, we omit the positive sign). For example, π=(5,−3,−2,1,4)
 is a signed permutation of length 5
.

Given: A positive integer n≤6
.

Return: The total number of signed permutations of length n
, followed by a list of all such permutations (you may list the signed permutations in any order).

Sample Dataset
2
Sample Output
8
-1 -2
-1 2
1 -2
1 2
-2 -1
-2 1
2 -1
2 1
"""


# Import packages
import itertools
import numpy as np


# Find signed permutations
n = 5
permutations = list(itertools.permutations(list(range(1, n+1)), n))
permutations2 = list(itertools.product([1, -1], repeat = n))
signed_permutations = []
for permut in permutations:
	signed_permut_tmp = [np.array(permut)*np.array(x) for x in permutations2]
	signed_permutations.extend(signed_permut_tmp)


# Print output
print(len(signed_permutations))
for permut in signed_permutations:
	permut = [str(x) for x in permut]
	print(" ".join(permut))
	

