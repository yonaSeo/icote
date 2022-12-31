import heapq

INF = int(1e9)

n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        now_dist, now = heapq.heappop(q)

        if distance[now] < now_dist:
            continue

        for i in graph[now]:
            node_num = i[0]
            node_dist = i[1]

            cost = now_dist + node_dist

            if cost < distance[node_num]:
                distance[node_num] = cost
                heapq.heappush(q, (cost, node_num))


dijkstra(start)

count = 0
max_dist = 0

for d in distance:
    if d != 1e9:
        count += 1
        max_dist = max(max_dist, d)

print(count - 1, max_dist)  # 시작 노드 제외해야 하므로 count - 1
