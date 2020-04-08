check_1 = 2000
check_2 = 2000

for i in range(3):
    a = int(input())
    if a <= check_1 :
        check_1 = a

for j in range(2):
    b = int(input())
    if b <= check_2 :
        check_2 = b

print(check_1+check_2-50)