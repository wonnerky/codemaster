import sys
string = sys.stdin.readline().strip()
string = string.upper()
alphabet = []
for i in string:
    if i not in alphabet:
        alphabet.append(i)
maxNum = 0
maxAlpa = None
state = 1
for i in alphabet:
    if string.count(i) > maxNum:
        maxAlpa = i
        maxNum = string.count(i)
    elif string.count(i) == maxNum:
        maxAlpa = '?'
        state = 0
print(maxAlpa)