
n = int(input())
ffibo_1 = 0
ffibo_2 = 1
cnt = 0
for i in range(n-1):
    ffibo_3 = ffibo_1 + ffibo_2
    ffibo_1 = ffibo_2
    ffibo_2 = ffibo_3

print(ffibo_2)