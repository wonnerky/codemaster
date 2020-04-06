import sys

number = []
mul = 1
for i in range(3):
    number.append(int(sys.stdin.readline()))
    mul = mul * number[i]
for i in range(10):
    print(str(mul).count(str(i)))