from itertools import permutations  # 순열 함수
import sys

N=int(sys.stdin.readline())
num_info=list(map(int,sys.stdin.readline().split()))

# 더하기가 몇갠지, 마이너스가 몇갠지 받는곳
plus, minus, mul, div = map(int, sys.stdin.readline().split())

#나중에 연산의 편의성을 위해 몇갠지 받은걸 펼침
oper_list=[]
oper_list=oper_list + [1]*plus #플러스는 '1'이라고 가정하고 개수만큼 넣어줌
oper_list=oper_list + [2]*minus
oper_list=oper_list + [3]*mul
oper_list=oper_list + [4]*div

#이제부터 나온 연산자로 뽑을 수 있는 경우의수 계산할거임

oper_set=[]
for i in list(permutations(oper_list)):
    oper_set.append(i)

oper_set=list(set(oper_set)) #같은 경우의 수 제거(같은 연산자의 순서만 바뀐걸 제거)

max_ans=-1e9
min_ans=1e9

for i in oper_set:

    final_ans=num_info[0] #처음 숫자

    for j in range(N-1): #연산자 개수만큼 반복
        if i[j] == 1: # 조합들 중에서 어떤 연산자인지
            final_ans = final_ans + num_info[j+1] # 다음수랑 더하기
        if i[j] == 2: # 조합들 중에서 어떤 연산자인지
            final_ans = final_ans - num_info[j+1] # 다음수랑 더하기
        if i[j] == 3: # 조합들 중에서 어떤 연산자인지
            final_ans = final_ans * num_info[j+1] # 다음수랑 더하기
        if i[j] == 4: # 조합들 중에서 어떤 연산자인지
            if final_ans<0:
                final_ans = -(-final_ans // num_info[i+1])
            else:
                final_ans = final_ans // num_info[j + 1]

    if max_ans < final_ans:
        max_ans=final_ans
    if min_ans > final_ans:
        min_ans=final_ans

print(max_ans)
print(min_ans)
