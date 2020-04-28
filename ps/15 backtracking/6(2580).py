import sys

sdk = []
for i in range(9):
    lst = list(map(int, sys.stdin.readline().split()))
    sdk.append(lst)

zeros = []
for i in range(9):
    for j in range(9):
        if sdk[i][j] == 0:
             zeros.append((i, j))

def num_po(i, j):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for k in range(9):
        if sdk[i][k] in num:
            num.remove(sdk[i][k])

    for k in range(9):
        if sdk[k][j] in num:
            num.remove(sdk[k][j])

    for a in range((i//3)*3, (i//3+1)*3):
        for b in range((j//3)*3, (j//3+1)*3):
            if sdk[a][b] in num:
                num.remove(sdk[a][b])

    return num

for k in range(len(zeros)):
    (i, j) = zeros[k]
    sdk[i][j] = num_po(i, j)

print(sdk)
