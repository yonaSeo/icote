def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [],  # 0번 인덱스는 진입 노드가 1번부터 시작하기 때문에 비워놓는다.
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 노드 크기만큼만 만들어서 각 인덱스 -1할 수도 있지만 하나 더 크게 만들고 0번 인덱스 비우는 편이 덜 헷갈린다.
visited = [False] * 9

dfs(graph, 1, visited)
