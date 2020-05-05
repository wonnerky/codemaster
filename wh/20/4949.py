import sys

# ( [ 가 나오면 list에 push
# ) ] 가 나오면 list에서 pop을 하고 해당 짝이 맞는지 비교
# no 조건 : pop을 할 수 없을 때(리스트가 비어 있음), pop이 짝이 아닐 때, 모든 검사 후 list가 비어 있지 않을 때
def checkBrackets(sentence):
    bracketList = []
    for character in sentence:
        if character == '(':
            bracketList.append(character)
        elif character == ')':
            if not bracketList or bracketList.pop() != '(':
                print('no')
                return
        elif character == '[':
            bracketList.append(character)
        elif character == ']':
            if not bracketList or bracketList.pop() != '[':
                print('no')
                return
    if not bracketList:
        print('yes')
    else:
        print('no')

sentences = []
while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == '.':
        break
    checkBrackets(sentence)

