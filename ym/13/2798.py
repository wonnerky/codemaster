n,m =map(int,input().split())

card = list(map(int,input().split()))

n=len(card)

sum_=0
for i in range(0, n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if card[i]+card[j]+card[k] >m:
                continue
            else:
                sum_=max(sum_,card[i]+card[j]+card[k])

print(sum_)