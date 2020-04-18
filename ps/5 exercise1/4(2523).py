a = int(input())

for i in range(1, 2*a):
    if i <= a:
        print("*"*i)

    else :
        print("*"*(2*a-i))
