"""
Problem
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

Sample Dataset
3
Sample Output
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""



n = int(input())
permut_list = ["1"]
for i in range(2, n+1):
    permuts_tmp = []
    for permut in permut_list:
        tmp = [permut[:x]+str(i)+permut[x:] for x in range(len(permut) + 1)]
        permuts_tmp.extend(tmp)
    permut_list = permuts_tmp
print(len(permut_list))
for permut in permut_list:
    print(permut.replace("", " ")[1:-1])
