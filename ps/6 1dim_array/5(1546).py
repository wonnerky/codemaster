a = int(input())
b = list(map(float, input().split()))

c = max(b)
for i in range(a):
    b[i] = (b[i]/c)*100

s = sum(b)
print(s/len(b))