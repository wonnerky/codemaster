import sys

def findNum(row):
    for i in range(1,10):
        if row.count(i) == 0:
            return i

def checkNum(list):
    count = 0
    for row in list:
        if row.count(0) == 1:
            index = row.index(0)
            row[index] = findNum(row)
        list[count] = row
        count += 1

def Matrix2Sqaure(flat):
    square = []
    for i in range(3):
        square.append(flat[3*i:3*i+3])

def sqaure2Matrix(square):
    flatList = []
    for i in square:
        flatList += i
    checkNum(flatList)
    return Matrix2Sqaure(flatList)

def getSquare2List(i,j):
    list_a = sudokuList[3 * i]
    list_b = sudokuList[3 * i + 1]
    list_c = sudokuList[3 * i + 2]
    list_a = list_a[3 * j:3 * j + 3]
    list_b = list_b[3 * j:3 * j + 3]
    list_c = list_c[3 * j:3 * j + 3]
    return list_a + list_b + list_c

def getList2Square(i,j,list):
    list_a = sudokuList[3 * i]
    list_b = sudokuList[3 * i + 1]
    list_c = sudokuList[3 * i + 2]
    list_a[3*j:3*j+3] = list[0:3]
    list_b[3*j:3*j+3] = list[3:6]
    list_c[3*j:3*j+3] = list[6:9]
    sudokuList[3 * i] = list_a
    sudokuList[3 * i + 1] = list_b
    sudokuList[3 * i + 2] = list_c


def checkSqaure():
    len = 3
    for i in range(3):
        for j in range(3):
            list = getSquare2List(i,j)
            if list.count(0) == 1:
                index = list.index(0)
                list[index] = findNum(list)
            getList2Square(i,j,list)

sudokuList = []
sudokuListColumn = []
sudokuListSquare = []
end = False

for i in range(9):
    sudokuList.append(list(map(int, sys.stdin.readline().split())))

while True:
    for i in range(9):
        if sudokuList[i].count(0) == 0:
            end = True
    if end:
        break
    checkNum(sudokuList)
    sudokuListColumn = [list(x) for x in zip(*sudokuList)]
    checkNum(sudokuListColumn)
    sudokuList = [list(x) for x in zip(*sudokuListColumn)]
    checkSqaure()



for i in range(9):
    for j in range(9):
        print(sudokuList[i][j],' ',end='')
    print()