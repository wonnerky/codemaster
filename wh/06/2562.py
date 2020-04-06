import sys

value = []
for i in range(9):
    value.append(int(sys.stdin.readline()))
print(max(value))
print(value.index(max(value))+1)