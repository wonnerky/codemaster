def merge(L, R):
    result = []
    while len(L) > 0 or len(R) > 0:
        if len(L) > 0 and len(R) > 0:
            if L[0] <= R[0]:
                result.append(L[0])
                L = L[1:]
            else:
                result.append(R[0])
                R = R[1:]
        elif len(L) > 0:
            result.append(L[0])
            L = L[1:]
        elif len(R) > 0:
            result.append(R[0])
            R = R[1:]
    return result

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    L_lst = lst[:len(lst)//2]
    R_lst = lst[len(lst)//2:]
    L_lst = merge_sort(L_lst)
    R_lst = merge_sort(R_lst)

    return merge(L_lst, R_lst)

import sys

a = int(sys.stdin.readline())
n_lst = []

for i in range(a):
    n_lst.append(int(sys.stdin.readline()))

sort_lst = merge_sort(n_lst)

for i in range(len(n_lst)):
    print(sort_lst[i])

