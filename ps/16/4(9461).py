def padovan(n):
    pdv = [0, 1, 1]

    if n >= 3:
        for i in range(3, n+1):
            pdv.append(pdv[i-3]+pdv[i-2])

    return pdv[n]

import sys

a = int(sys.stdin.readline())

for i in range(a):
    print(padovan(int(sys.stdin.readline())))
