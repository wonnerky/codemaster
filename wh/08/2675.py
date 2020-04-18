import sys
total = int(sys.stdin.readline())
inputs = []
for i in range(total):
    inputs.append(sys.stdin.readline().split())
for i in range(total):
    for char in inputs[i][1]:
        print(char*int(inputs[i][0]),end='')
    print()