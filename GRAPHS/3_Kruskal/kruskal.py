def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):  # 모든 간선에 대한 정보 입력 받기
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))  # 비용 순 정렬 위해 튜플 첫 원소 비용으로 설정

edges.sort()  # 간선 비용 오름차순 절렬

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):  # 사이클 발생 안 할 경우 집합 포함
        union_parent(parent, a, b)
        result += cost

print(result)
