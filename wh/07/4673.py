def posSum(str):
    sum = 0
    for i in str:
        sum += int(i)
    return sum

a = list(range(1, 10000))

for i in range(1, 10000):
    num = i+posSum(str(i))
    if a.count(num) > 0:
        a.remove(i+posSum(str(i)))

for i in range(len(a)):
    print(a[i])