import sys
numbers = sys.stdin.readline().split()
i = 0
for number in numbers:
    numbers[i] = int(number[::-1])
    i += 1
if numbers[0] > numbers[1]: print(numbers[0])
else: print(numbers[1])