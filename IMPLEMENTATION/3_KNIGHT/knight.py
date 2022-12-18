location = input()
cnt = 0

row = int(location[1])
col = int(ord(location[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2,), (-1, 2), (1, -2), (1, 2)]

for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if next_row < 1 or next_row > 8 or next_col < 1 or next_col > 8:
        continue
    cnt += 1

print(cnt)

# x = int(location[1])
# y = location[0]

# col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]

# for i in range(len(col)):
#     if y == col[i]:
#         y = i + 1

# for i in range(4):
#     nx = x + (dx[i]*2)
#     ny = y + (dy[i]*2)
#     if nx < 1 or ny < 1 or nx > 8 or ny > 8:
#         continue
#     if dx[i] == 0:
#         if nx + 1 <= 8:
#             cnt += 1
#         if nx - 1 >= 1:
#             cnt += 1
#     if dy[i] == 0:
#         if ny + 1 <= 8:
#             cnt += 1
#         if ny - 1 >= 1:
#             cnt += 1

# print(cnt)