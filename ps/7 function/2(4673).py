import math

def non_self_num(a):
    c = 0
    keep = a
    while a!=0:
        b = a % 10
        c = b + c
        a = math.trunc(a/10)

    return c + keep

n_1 = set(range(1,10001))
n_2 = set()

for i in range(1, 10001):
    n_2.add(non_self_num(i))

sel_num_set = n_1 - n_2

for i in sorted(sel_num_set):
    print(i)
