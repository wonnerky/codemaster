import sys

def calPeople(k,n):
    if k == 0:
        people = n
    else:
        people = 0
        for i in range(n):
            people += calPeople(k-1, i+1)
    return people

n = int(sys.stdin.readline().strip())
for i in range(n):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    people = calPeople(k,n)
    print(people)