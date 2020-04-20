import sys

a = int(sys.stdin.readline())

for i in range(a):
    b = list(map(int, sys.stdin.readline().split()))
    std_num = b[0]
    del b[0]
    avg_score = sum(b)/std_num
    cnt = 0

    for j in range(len(b)):
        if avg_score < b[j]:
            cnt += 1
    print("%.3f%%" %(cnt/std_num*100))