a = int(input())
b = int(input())
c = int(input())

d = list(map(int, list(str(a * b * c))))

for i in range(10):

    print(d.count(i))