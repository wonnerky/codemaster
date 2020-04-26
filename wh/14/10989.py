import sys
'''
메모리 크기를 고려해야 한다.
list에 전부 넣어선 메모리 초과가 나온다.
'''


# def getDict(key):
#     if numDict.get(key) is None:
#         numDict[key] = 0
#     numDict[key] += 1
#
# numDict = {}
# for _ in range(int(sys.stdin.readline())):
#     getDict(int(sys.stdin.readline().strip()))
# keys = list(numDict.keys())
# keys.sort()
# for i in range(len(keys)):
#     for j in range(numDict[keys[i]]):
#         print(keys[i])

numbers = [0] * 10001
for _ in range(int(sys.stdin.readline())):
    numbers[int(sys.stdin.readline().strip())] += 1
for i in range(1, 10001):
    for j in range(numbers[i]):
        print(i)
