import sys
n = sys.stdin.readline()
numbers = sys.stdin.readline().strip()
sum = 0
for number in numbers:
    sum += int(number)
print(sum)