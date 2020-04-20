import sys

num_cnt, num_max = map(int, sys.stdin.readline().split())
num_in = list(map(int, sys.stdin.readline().split()))

sum_list = []

if num_cnt >= 3 and num_cnt == len(num_in):
    for i in range(len(num_in)):
        for j in range(len(num_in)):
            for h in range(len(num_in)):
                if h != i and h != j and i != j:
                    sum_list.append(num_in[i]+num_in[j]+num_in[h])

    for k in range(len(sum_list)):
        if sum_list[k] > num_max:
            sum_list[k] = 0
    print(max(sum_list))

else:
    sys.exit()