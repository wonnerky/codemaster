a = int(input())

for i in range(a):
    sol = list(map(str, input()))
    c = 0
    score = 0
    for j in range(len(sol)):
        if sol[j] == 'O':
            c = c+1
            score = score + c
        else :
            c = 0

    print(score)