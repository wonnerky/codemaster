import sys

def checkMatrix(Matrix, row, column):
    _B = 0
    _W = 0
    _minB = 99
    _minW = 99
    for i in range(column - 7):
        for j in range(row - 7):
            for l in range(8):
                for k in range(8):
                    _B += checkColor(Matrix[j+l][i+k], l, k, 'B')
                    _W += checkColor(Matrix[j+l][i+k], l, k, 'W')
            if _minB > _B: _minB = _B
            if _minW > _W: _minW = _W
            _B = 0
            _W = 0
    if _minB <= _minW: print(_minB)
    else: print(_minW)

def checkColor(color, row, column, label):
    # 짝수면
    if row % 2 == 0:
        if column % 2 == 0:
            if label != color:
                return 1
        else:
            if label == color:
                return 1
    else:
        if column % 2 == 0:
            if label == color:
                return 1
        else:
            if label != color:
                return 1
    return 0

row, column = map(int, sys.stdin.readline().split())
if row < 8 and column < 8:
    exit()
chessMatrix = []
for i in range(row):
    chessMatrix.append(sys.stdin.readline().strip())
checkMatrix(chessMatrix,row,column)