INF = int(1e9)

n, m = map(int, input('노드 & 간선 개수').split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 2차원 리스트(그래프) 만들고 무한으로 초기화

for a in range(1, n + 1):  # 자기 자신으로 가는 비용은 0으로 초기화
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):  # 각 간선에 대한 정보 입력 받아 그 값으로 초기화
    a, b, c = map(int, input('a 노드에서 b로 가는 비용 c').split())
    graph[a][b] = c

for k in range(1, n + 1):  # 점화식 따라 FW 알고리즘 수행
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print('도달 불가능', end=" ")
        else:
            print(graph[a][b], end=" ")
        print()
