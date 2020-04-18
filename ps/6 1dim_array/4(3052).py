c = list()
for i in range(10):
    a = int(input())
    b = a % 42
    c.append(b)
c = set(c)
print(len(c))
