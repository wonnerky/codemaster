def isHansu(num):
    num = str(num)
    l = []
    k = []
    for i in num:
        l.append(int(i))
    for i in range(len(l)-1):
        k.append(l[i] - l[i+1])
    if compare(k):
        return 1
    else: return 0


def compare(lis):
    cp = lis[0]
    for i in lis:
        if cp != i:
            return 0
    return 1


n = int(input())
cnt = 99
if n < 100:
    print(n)
else:
    for i in range(100,n+1):
        cnt += isHansu(i)
    print(cnt)