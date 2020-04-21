a = int(input())

for i in range(1, a+1):
    if a % 2 == 1:
        print("* "*(a//2+1))
        print(" *"*(a//2))

    else :
        print("* "*(a//2))
        print(" *"*(a//2))