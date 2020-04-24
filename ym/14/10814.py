import sys

n=int(sys.stdin.readline()) #몇번 반복
info=[]
for i in range(n):
    info.append(sys.stdin.readline().split())
    info[i][0]=int(info[i][0]) #info=[[나이,이름],[나이,이름]]
    info[i].append(i) #순서 명시 #info=[[나이,이름,순서],[나이,이름,순서]]

new_info=sorted(info, key=lambda x : (x[0],x[2])) #나이우선, 순서우선

for i in range(n):
    print(new_info[i][0],new_info[i][1])

