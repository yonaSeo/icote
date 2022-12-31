import heapq

INF = int(1e9)

n, m = map(int, map(int, input("노드 & 간선 개수").split()))
start = int(input("시작 노드"))

graph = []  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
distance = [INF] * (n + 1)  # 최단 거리 테이블 모두 무한으로 초기화

for _ in range(m):  # 모든 간선 정보 입력받기
    a, b, c = int(map(input('출발 노드 & 도착 노드 & 거리')))
    graph[a].append((b, c))  # a번 노드의 b번 노드로 가는 거리가 c라는 의미


# 기억해야 할 것은 이것이 '시작 노드'로부터 '목표 노드'까지의 최단거리를 알아내는 알고리즘이라는 것이다.
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # PQ 시작 노드 초기화 -> 튜플로 설정 시 첫 번째 값을 기준으로 힙 구성
    distance[start] = 0  # 테이블 시작 노드 초기화

    while q:  # 큐가 비어있지 않다면
        now_dist, now = heapq.heappop(q)  # 가장 최단 거리 짧은 노드 추출

        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        # -> 즉 테이블에 현재 노드까지의 최단 거리(distance[now])가 기록되어 있으며 (INF가 아니며)
        # -> 그 거리가 PQ에서 '지금' 꺼낸 현재 거리(now_dist)보다 작은 경우 (더 낮은 value가 선 처리됨)
        if distance[now] < now_dist:
            continue

        for i in graph[now]:  # 현재 노드와 연결된 다른 노드 x(의 정보)를 확인
            node_num = i[0]  # 현재 노드의 이름
            node_dist = i[1]  # 현재 노드의 노드 x까지의 거리

            # 시작 노드에서부터 현재 노드까지의 거리(now_dist)와
            # 현재 노드의 노드 x까지의 거리(node_dist)를 더해서
            # 시작 노드에서 부터 노드 x까지의 거리(cost)를 계산
            cost = now_dist + node_dist

            # 시작노드 -> 현재 노드 -> 노드 x로 이동하는 거리(cost)와
            # 시작노드 -> 임의의 다른 경로 or None -> 노드 x로 이동하는 거리(distance[node_num])
            # 둘을 비교해서 전자가 더 짧으면, 기존의 노드 x로 가는 최단거리를 전자로 갱신하고
            # PQ에 노드 x로의 최단경로로 등록 (이때 같은 노드가 있으면 value가 더 낮은 노드가 '우선'된다)
            if cost < distance[node_num]:
                distance[node_num] = node_dist
                heapq.heappush(q, (cost, node_num))


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print('도달 불가능')
    else:
        print(distance[i])
