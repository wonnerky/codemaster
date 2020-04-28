import sys

triangle = int(sys.stdin.readline()) #5
triangle_matrix = []

max_matrix = [[] for _ in range(triangle)] #5

for _ in range(triangle):
    triangle_matrix.append(list(map(int, sys.stdin.readline().split()))) #5

print(triangle_matrix)

#역순으로 하위 항목을 모두 더한 최댓값을 저장
for i in range(triangle-1, -1, -1): #4,3,2,1,0
    for j in range(len(triangle_matrix[i])): #0 1 2 3 4
        if i == triangle-1: # 4==4

            print(triangle_matrix[i][j])

            max_matrix[i].append(triangle_matrix[i][j]) # max[첫번째] = triangle[4][4] 마지막
        else:
            max_matrix[i].append(triangle_matrix[i][j] + max(max_matrix[i+1][j], max_matrix[i+1][j+1]))
            #print(triangle_matrix[i][j])
print(max_matrix[0][0])