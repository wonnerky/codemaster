M = int(input())
N = int(input())


def is_prime(num):
    if (num <= 1):
        return False

    i = 2
    while i * i <= num:
        if num % i == 0:
            return False

        i += 1
    return True


sum = 0
minv = 0

for i in range(M, N + 1):
    if (is_prime(i)):
        sum += i
        if (minv == 0 or minv > i):
            minv = i

if (sum == 0):
    print(-1)
else:
    print(sum)
    print(minv)