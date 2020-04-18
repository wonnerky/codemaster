a, b, c = map(int, input().split())

if 1 <= a and b and c <= 10000:

    print((a+b)%c)
    print(((a%c)+(b%c))%c)
    print((a*b)%c)
    print(((a%c)*(b%c))%c)