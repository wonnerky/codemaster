import sys

def checkGroup(word):
    if list(word) != sorted(word, key=word.find):
        print(sorted(word,key=word.find))
        return 0
    return 1


n = int(sys.stdin.readline())
total = 0
for i in range(n):
    word = sys.stdin.readline().strip()
    total += checkGroup(word)
print(total)

'''
수정 전
import sys
def checkGroup(word):
    past = None
    checkList = []
    for i in word:
        if past != i:
            if i in checkList:
                return 0
            else: checkList.append(i)
            past = i
    return 1


n = int(sys.stdin.readline())
total = 0
for i in range(n):
    word = sys.stdin.readline()
    total += checkGroup(word)
print(total)
'''