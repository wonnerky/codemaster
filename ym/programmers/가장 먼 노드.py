def solution(n:int, edge:int)->int:
    graph =[[] for _ in range(n)]
    distances = [ 0 for _ in range(n) ]
    is_visited = [False for _ in range(n)]
    # 시작 노드 방문
    queue = [0]
    is_visited[0] = True
    # 노드 연결
    for (a,b) in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    # queue 이용 distance 계산
    while queue:
        i = queue.pop(0)
        # i에서 갈수 있는 j
        for j in graph[i]:
            if is_visited[j] == False:
            	# 갈 수 있으면 앞의 점까지의 거리 + 거리를 1 씩 더한다
                # 시작점의 거리는 0으로 초기화되어 있다.
                is_visited[j] = True
                queue.append(j)
                distances[j] = distances[i] + 1
    answer = distances.count(max(distances))
    # max 값의 수를 센다.
    return answer