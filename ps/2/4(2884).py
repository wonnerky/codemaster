h, m = map(int, input().split())

if 0 <= m <45 :
    m = 60 + (m-45)
    if 1 <= h <= 23 :
        h = h-1
    elif h == 0:
        h = 24 - 1
else :
    m = m-45
print(h,m)


