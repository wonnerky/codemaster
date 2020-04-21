a = int(input())

s_list = []

for _ in range(a):
    w, h = map(int, input().split())
    s_list.append((w, h))

for i in s_list:
    r = 1
    for j in s_list:
        if i[0] < j[0] and i[1] < j[1]:
            r += 1

    print(r, end = " ")

