import sys

def findMax(steps, number):
    def checkMax(index):
        return maxCont[index] if maxCont[index] >= maxDisCont[index] else maxDisCont[index]
    maxCont = [0] * number
    maxDisCont = [0] * number
    for i in range(number):
        if i == 0:
            maxCont[i] = steps[i]
            maxDisCont[i] = steps[i]
        elif i == 1:
            maxCont[i] = steps[i-1] + steps[i]
            maxDisCont[i] = steps[i]
        # index 2부터 Continuous 와 DisContinuous 를 고려. Continuous 는 i-1의 Discontinuous 값
        # Discontinuous 는 i-2의 max 값
        else:
            maxCont[i] = maxDisCont[i-1] + steps[i]
            maxDisCont[i] = checkMax(i-2) + steps[i]
    print(maxCont[-1] if maxCont[-1] > maxDisCont[-1] else maxDisCont[-1])


n = int(sys.stdin.readline().strip())
steps = [int(sys.stdin.readline().strip()) for _ in range(n)]
findMax(steps, n)
