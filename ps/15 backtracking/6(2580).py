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


flag = False


def answer(lst):
    global flag
    for i in range(9):
        if set(lst[i]) == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            flag = True
            return flag

def sudoku(x):
    if x == len(zeros):
        if answer(sdk) == True:
            return sdk
        else :


    else :
        (i, j) = zeros[x]
        crr_num = num_po(i, j)

        for nn in crr_num:
            sdk[i][j] = nn
            sudoku(x+1)


for r in sdk:
    print(*r)
