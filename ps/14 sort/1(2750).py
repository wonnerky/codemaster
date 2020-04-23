a = int(input())
num_list = []
for i in range(a):
    num_list.append(int(input()))

num_sort = sorted(num_list)
for i in num_sort:
    print(i)