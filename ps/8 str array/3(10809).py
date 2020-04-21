#acsci code a=97 / z=122
alpha = list(range(97, 123))

text = list(input())
text_asc = []

for i in text:
    text_asc.append(ord(i))

for i in range(len(alpha)):
    if alpha[i] in text_asc:
        alpha[i] = text_asc.index(alpha[i])
    else:
        alpha[i] = -1

for i in alpha:
    print(i, end=' ')