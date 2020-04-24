
from functools import reduce
import sys

n=int(sys.stdin.readline())
#ans=reduce(lambda x,y: x+y, [i for i in range(n+1)])

empty=[0]*int(n+1) #10자리
#print(empty)

empty[1]=1
#print(empty)

for i in range(2,n+1): #2~10
    empty[i]=empty[i-1]+empty[i-2]
    print(empty)
print(empty[-1])

import sys

N = int(sys.stdin.readline())
arr = [0 for _ in range(N+1)]
arr[1] = 1

for i in range(2, N+1):
    arr[i] = arr[i-1] + arr[i-2]
    print(arr)
print(arr[-1])