n = int(input())
plans = list(map(str, input().split()))

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    nx, ny = 0, 0
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            break
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x = nx
    y = ny

print(x, y)

# x, y = 1, 1
# dx, dy = [], []

# for d in plans:
#     if d == "L":
#         dx.append(0)
#         dy.append(-1)
#     elif d == "R":
#         dx.append(0)
#         dy.append(1)
#     elif d == "U":
#         dx.append(-1)
#         dy.append(0)
#     elif d == "D":
#         dx.append(1)
#         dy.append(0)

# for i in range(len(plans)):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if nx >= 1 and nx <= n and ny >= 1 and ny <= n:
#         x = nx
#         y = ny

# print(x, y)