a = int(input())   #a=97 / z=122

for i in range(a):
    b, c = input().split()
    text = ''
    for i in c:
        text += int(b)*i
    print(text)