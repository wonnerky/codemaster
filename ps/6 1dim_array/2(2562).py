b = list()

for i in range(9):
    a = int(input())
    b.append(a)

print('{}'.format(max(b)))
c = b.index(max(b))
print(c+1)