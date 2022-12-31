from collections import deque

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
indegree = [0] * (v + 1)  # 진입차수 초기화

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # 노드 A에서 노드 B로 이동 가능
    indegree[b] += 1  # 노드 B의 진입차수 + 1


def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):  # 진입 차수 0인 노드 큐에 삽입
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()  # 큐에서 노드 꺼내서
        result.append(now)  # 결과 리스트에 추가

        for i in graph[now]:
            indegree[i] -= 1  # 현재 노드와 연결된 노드들의 진입차수 - 1
            if indegree[i] == 0:  # 새롭게 진입차수 0 되는 노드 큐에 삽입
                q.append(i)

    for i in result:
        print(i, end=" ")


topology_sort()
