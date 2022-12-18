def dfs(x, y):
    if x <= -1 or y <= -1 or x >= m or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        # du
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
    graph[i].append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        if dfs(n, m) == True:
            result += 1

print(result)
