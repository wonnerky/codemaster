import sys

def findBag(kilo):
    a = int(kilo / 5)
    for i in range(a+1):
        b = (kilo - ((5 * (a - i)))) / 3
        if (b - int(b)) == 0:
            return print(int(a-i+b))
    return print(-1)


kilo = int(sys.stdin.readline().strip())
if kilo == 0:
    print(-1)
else: findBag(kilo)
