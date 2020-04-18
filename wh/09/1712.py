import sys

def breakEvenPoint(fc,pc,pp):
    print(int(fc/(pp-pc) + 1))


fixedCost, prodCost, prodPrice = map(int, sys.stdin.readline().split())
if prodCost < prodPrice:
    breakEvenPoint(fixedCost, prodCost, prodPrice)
else:
    print(-1)