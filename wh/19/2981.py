import sys

# 약수 구하는 함수
def cdList(x):
    cd_list = [x]
    for i in range(2, int(x**(1/2) + 1)):
        if x % i == 0:
            cd_list.append(i)
            if x//i != i:
                cd_list.append(x//i)
    cd_list.sort()
    return cd_list


numbers = [int(sys.stdin.readline().strip()) for _ in range(int(sys.stdin.readline()))]
numbers.sort()
min = 1000000000
# 입력 받은 수 중에서 두개의 차이가 가장 작은 수보다 작은 수로 답이 구해진다
for i in range(len(numbers)-1):
    gap = abs(numbers[i] - numbers[i + 1])
    if min > gap:
        min = gap
        # 차이가 가장 작은 수 구하기

# 가장 작은 수에서 해당 문제를 만족하는 제일 큰 수가 해당 문제의 최대 공약수
for i in reversed(range(min+1)):
    criteria = numbers[0] % i
    for number in numbers[1:]:
        if number % i != criteria:
            break
        if number == numbers[-1]:
            # i가 문제를 만족하는 가장 큰 수일 때, 그 수의 공약수들을 출력
            for j in cdList(i):
                print(j, end=' ')
            exit()