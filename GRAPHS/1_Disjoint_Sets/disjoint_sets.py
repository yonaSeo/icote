# 특정 원소가 속한 집합 찾기
# (실제로는 루트까지 찾지만 관행적으로 parent로 명시)
def find_parent(parent, x):
    if parent[x] != x:  # 루트 노드(parent[x]가 x 자신인 노드 x) 찾을 때까지 재귀 호출
        parent[x] = find_parent(parent, parent[x])  # 부모 노드만 찾는 것이 아니라 루트 노드로 갱신
    return parent[x]


#       return find_parent(parent, parent[x])
#   return x


# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())  # 노드 개수와 간선(Union 연산)의 개수
parent = [0] * (v + 1)

for i in range(1, v + 1):  # 부모 테이블에서 부모를 자기 자신으로 초기화
    parent[i] = i

for i in range(e):  # 간선 개수 만큼 Union 연산을 각각 수행
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print("각 원소가 속한 집합: ", end="")
for i in range(1, v + 1):
    print(find_parent(parent, 1), end=" ")  # 루트 노드 반환

print()

print("부모 테이블: ", end="")
for i in range(1, v + 1):
    print(parent[i], end=" ")
