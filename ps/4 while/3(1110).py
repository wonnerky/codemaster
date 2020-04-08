i = 0
a = int(input())
check = a
b = 0

while True:
    b = (a % 10)*10 + (a//10 + a % 10) % 10
    i = i+1
    a = b
    if check == b:
        break

print(i)
