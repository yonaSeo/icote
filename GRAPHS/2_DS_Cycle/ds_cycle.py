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

for i in range(1, v + 1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    # 사이클 발생 시 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:  # 사이클 발생 안할 시 합집합 연산 수행
        union_parent(parent, a, b)

if cycle:
    print("사이클 발생했시유!")
else:
    print("사이클 안 발새유ㅠㅠ")
