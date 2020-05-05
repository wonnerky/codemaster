import sys

# list의 순서를 다시 정렬
# 프린터 첫 번째 순서의 중요도가 제일 크지 않으면, 맨 뒤로 보내기
# 프린터의 첫 번째 순서의 중요도가 제일 크면 pop 하고 정렬된 리스트에 append
# 정렬 된 리스트 반환 후 확인하고 싶은 문서의 순서를 인덱스로 알 수 있다.
# 전부 정렬 후 순서를 찾기 때문에 비효율이 있을 수 있다. 개선 가능
def sortOrder(printOrder, importance):
    initList = printOrder
    orderedList = []

    while initList:
        for i in initList:
            if importance[initList[0]] < importance[i]:
                temp = initList.pop(0)
                initList.append(temp)
                break
            if len(initList) == 1 or i == initList[-1]:
                orderedList.append(initList.pop(0))
    return orderedList


case = int(sys.stdin.readline().strip())
for _ in range(case):
    n, m = map(int, sys.stdin.readline().split())
    importance = list(map(int, sys.stdin.readline().split()))
    printOrder = [i for i in range(n)]
    orderedList = sortOrder(printOrder, importance)
    place = 1 + orderedList.index(m)
    print(place)
