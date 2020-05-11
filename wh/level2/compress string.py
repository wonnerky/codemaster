def solution(s):
    if len(s) == 1:
        return 1
    answer = 1000
    for i in range(1,int(len(s)/2)+1):
        cnt = 0
        cntList = []
        for j in range(0,len(s)-i,i):
            if s[j:j+i] == s[j+i:j+i*2]:
                cnt += 1
            else:
                if cnt != 0:
                    cntList.append(cnt)
                cnt = 0
        if cnt != 0:
            cntList.append(cnt)
            cnt = 0
        value = 0
        digit = []
        if cntList:
            value = i*sum(cntList)
            for k in cntList:
                if (k+1) // 10 == 0:
                    digit.append(1)
                elif (k+1) // 10 < 10:
                    digit.append(2)
                elif (k+1) // 10 < 100:
                    digit.append(3)
                else:
                    digit.append(4)
        newAns = len(s) - value + sum(digit)
        if answer > newAns: answer = newAns
    return answer

s = "gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg" \
    "gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg" \
    "gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg" \
    "gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg" \
    "gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg" \
    "gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg" \
    "gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg" \
    "gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg" \
    "gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg" \
    "gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
print(len(s))
print(solution(s))