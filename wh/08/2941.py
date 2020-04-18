import sys
croAlpa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
croAlpaCount = 0
word = sys.stdin.readline().strip()
wordOriginal = word
for key in croAlpa:
    if wordOriginal.find(key) != -1:
        if word.find(key) != -1:
            croAlpaCount += word.count(key)
            word = word.replace(key,'')
print(len(word)+croAlpaCount)