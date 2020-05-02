import sys

n, value = map(int, sys.stdin.readline().split())
valueList = [int(sys.stdin.readline().strip()) for _ in range(n)]
coins = 0

# coin 개수를 count
for i in reversed(valueList):
    # value를 coin크기로 나누기 // value list의 역순으로 검증. 큰 값부터 뺀다.
    coin = value // i
    # value가 coin으로 나눠지면
    if coin != 0:
        # value update
        value -= (coin * i)
        # coin 개수 update
        coins += coin
print(coins)