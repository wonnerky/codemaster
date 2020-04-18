a = int(input())

for i in range(a):
    cnt = 0
    std_list = list(map(int, input().split()))
    avg = sum(std_list[1:])/std_list[0]
    for j in range(1, len(std_list)):
        if avg < std_list[j]:
            cnt = cnt + 1

    print(str(round(cnt/std_list[0]*100, 3))+'%')