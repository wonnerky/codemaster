<<<<<<< HEAD
import sys
from collections import Counter

n=int(sys.stdin.readline())


def average(s):

    return sum(s)//len(s)

def mid(s):
    s=sorted(s)
    where=len(s)//2
    return s[where]

def count(s):
    cnt= Counter(s)

    if len(cnt.most_common(1)) > 1:
        return cnt.most_common()[-2][0]
    else:
        return cnt.most_common(1)[0][0]

def how_far(s):
    return abs(max(s)-min(s))

s=[]
for i in range(n):
    new_num=int(sys.stdin.readline())
    s.append(new_num)

print(average(s))
print(mid(s))
print(count(s))
print(how_far(s))






=======
import sys
from collections import Counter

n=int(sys.stdin.readline())


def average(s):

    return sum(s)//len(s)

def mid(s):
    s=sorted(s)
    where=len(s)//2
    return s[where]

def count(s):
    cnt= Counter(s)

    if len(cnt.most_common(1)) > 1:
        return cnt.most_common()[-2][0]
    else:
        return cnt.most_common(1)[0][0]

def how_far(s):
    return abs(max(s)-min(s))

s=[]
for i in range(n):
    new_num=int(sys.stdin.readline())
    s.append(new_num)

print(average(s))
print(mid(s))
print(count(s))
print(how_far(s))






>>>>>>> 8893303b5576737fdd24129b31c136a7fd005dfe
