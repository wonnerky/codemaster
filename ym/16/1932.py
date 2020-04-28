import sys
t = int(sys.stdin.readline()) #5
n=[list(map(int,sys.stdin.readline().split())) for _ in range(0,t)]

print(n)

dp=[]

for i in range(1,t): #1,2,3,4
    for j in range(len(n[i])): #[(7)0,1] [(3,8)0,1,2], []
        if j == 0 :
            n[i][j] += (n[i-1][j]) #7+3, 7+8

        elif j==i: #j==1, i==1 #j==1,i==1
            n[i][j] +=(n[i-1][j-1])
            print(n)
        else :
            n[i][j] += (max(n[i-1][j],n[i-1][j-1]))

print(max(n[t-1]))


'''
일단 입력을 다 배열로 받고

[7]

[3,8]

[8,1,0]

[2,7,4,4]

[4,5,2,6,5]

 

위에서 부터 대각선에 해당하는 값을 아래에 더해주며 내려온다.

그럼

---

[7]

[10,15]

---

 

이런식으로 시작을 할텐데

문제는 3,8 에서 8,1,0이 있는 행으로 내려올때 1이 3과 8 양쪽의 대각선에 해당된다.

이럴 땐 max로 해결해줌

 

[7]

[10,15]

[18,max([11],[16]),15]

---

이런식으로 쭉 내려오다 보면 제일 마지마지막 줄에서 가장 큰값이 최댓값이 되겠다



'''




