def dfs(x, y):
    if x <= -1 or y <= -1 or x >= m or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 아래의 모든 리턴값(False)들은 사용되지 않으므로, 단지 인덱스값만 업데이트될 뿐이다.
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


n, m = map(int, input().split())
graph = []
result = 0
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드에 대하여 음료수 채우기
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
