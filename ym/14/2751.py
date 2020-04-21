import sys

n= int(sys.stdin.readline())
s=[]
for i in range(n):
    a=int(sys.stdin.readline())
    s.append(a)

#ex: [6,5,3,1,8,7,2,4]
def merge(s):
    if len(s)<2:
        return s

    mid = len(s)//2 #중간피봇지정

    low_arr = merge(s[:mid]) #중간 이하
    high_arr = merge(s[mid:]) #중간 이상

    merged_arr=[]
    l=0
    h=0

    while l <len(low_arr) and h<len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])

            l+=1
        else:
            merged_arr.append(high_arr[h])

            h+=1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]

    return merged_arr


for i in merge(s):
    print(i)






