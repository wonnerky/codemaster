#sum = 0

#for i in range(5):
#    a = int(input())
#    if a <= 40 :
#        a = 40
#    sum = sum + a

#print(int(sum/5))

score_list = []

for i in range(5):
    score = int(input())
    if score < 40:
        score_list.append(40)
    else:
        score_list.append(score)

print(round(sum(score_list)/5))
