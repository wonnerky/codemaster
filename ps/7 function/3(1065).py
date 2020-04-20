def hansu(n):
    a = []
    b = []

    if 0 < n < 10:
        return 0

    elif n >= 0:
        for i in str(n):
            a.append(int(i))
            for j in range(1, len(a)):
                b.append(a[j]-a[j-1])
        return (sum(b)-max(b)*len(b))

n_1 = int(input())
cnt = 0

for i in range(1, n_1+1):
    if hansu(i) == 0:
        cnt += 1

print(cnt)