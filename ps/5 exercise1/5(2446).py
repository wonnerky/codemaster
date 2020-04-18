a = int(input())

for i in range(1, 2*a):
    if i <= a:
        print(" "*(i-1)+"*"*(2*(a-i)+1))

    else :
        print(" "*(2*a-i-1)+"*"*(2*(i-a)+1))