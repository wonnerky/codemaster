import sys

n = int(sys.stdin.readline().strip())
max = 0
j = 0
if n > 10000:
    exit()
else:
    for i in range(n):
        while True:
            j += 1
            if '666' in str(j):
                if max < j:
                    max = j
                    break
print(max)