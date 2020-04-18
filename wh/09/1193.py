import sys

order = int(sys.stdin.readline().strip())
line = 1
while 2*order > line * (line + 1):
    line += 1

loc = order - ((line * (line - 1))/2)

if (line % 2) == 0:
    upper = int(loc)
    bottom = int(line - loc + 1)
else:
    upper = int(line - loc + 1)
    bottom = int(loc)

print(str(upper) + '/' + str(bottom))