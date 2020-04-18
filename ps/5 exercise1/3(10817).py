a = list(map(int, input().split(' ')))

for i in range(len(a)):
    a[i] = int(a[i])

sort_list = sorted(a)
print(sort_list[1])