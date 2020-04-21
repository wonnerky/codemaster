import sys

n = int(sys.stdin.readline().strip())
memberList = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    memberList.append((age, name))

memberList.sort(key=lambda member: member[0])
for age, name in memberList:
    print(age , name)
