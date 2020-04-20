tri_f = int(input())

tri_a = []
for i in range(tri_f):
    tri_a.append(list(map(int, input().split())))

s = 0
f = 1
sum_list = []
for i in range(tri_f):
    for j in range(f):
        if i == 0:
            s = tri_a[i][i]
        elif i >= 1 and j

    f += 1


print(tri_a)