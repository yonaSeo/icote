INF = int(1e9)

n, m = map(int, input('노드 개수 & 간선 개수').split())
start = int(input('시작 노드 번호'))

graph = [[] for i in range(n + 1)]  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
visited = [False] * (n + 1)  # 방문한 적이 있는지 체크하는 목적의 리스트
distance = [INF] * (n + 1)  # 최단 거리 테이블 모두 무한으로 초기화

for _ in range(m):  # 모든 간선 정보 입력받기
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a번 노드의 b번 노드로 가는 거리가 c라는 의미


def get_smallest_node():  # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호 반환
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


# 기억해야 할 것은 이것이 '시작 노드'로부터 '목표 노드'까지의 최단거리를 알아내는 알고리즘이라는 것이다.
def dijkstra(start):
    distance[start] = 0  # 시작 노드 초기화
    visited[start] = True  # 여기서 방문처리했기 때문에 다시 방문 안 한다.

    # 시작 노드의 (b, c)'들'을 가져와 각 노드들을 인덱스로 하는 테이블에 각각의 거리 c 할당
    for i in graph[start]:
        distance[i[0]] = i[1]

    for _ in range(n - 1):  # 시작 노드 제외한 전체 n - 1개의 노드에 대해 반복
        now = get_smallest_node()  # 현재 최단 거리가 가장 짧은 노드를 꺼내서,
        visited[now] = True  # 방문처리

        for i in graph[now]:  # 현재 노드와 연결된 다른 노드 x(의 정보)를 확인
            node_num = i[0]  # 현재 노드의 이름
            node_dist = i[1]  # 현재 노드의 노드 x까지의 거리

            # 시작 노드에서부터 현재 노드까지의 거리(distance[now])와
            # 현재 노드의 노드 x까지의 거리(node_dist)를 더해서
            # 시작 노드에서 부터 노드 x까지의 거리(cost)를 계산
            cost = distance[now] + node_dist

            # 시작노드 -> 현재 노드 -> 노드 x로 이동하는 거리(cost)와
            # 시작노드 -> 임의의 다른 경로 or None -> 노드 x로 이동하는 거리(distance[node_num])
            # 둘을 비교해서 전자가 더 짧으면, 기존의 노드 x로 가는 최단거리를 전자로 바꿈
            if cost < distance[node_num]:
                distance[node_num] = cost


dijkstra(start)

for i in range(1, n + 1):  # 모든 노드로 가는 최단 거리 출력
    if distance[i] == INF:
        print("도달 불가능")
    else:
        print(distance[i])
