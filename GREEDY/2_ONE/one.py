n, k = map(int, input().split())
cnt = 0

while True:
    # N이 K로 나눠지는 수가 될 때까지 빼기
    target = (n // k) * k
    cnt += n - target
    n = target
    # N이 K보다 작아지면 (더 이상 나눌 수 없으면) 탈출
    if n < k:
        break
    # N을 K로 나누기
    n //= k
    cnt += 1
# 마지막으로 남은 수에 대하여 1씩 빼기
cnt += (n - 1)
print(cnt)

# 그런데 정확히 말해서 마지막 나눌 수 없는 수에 도달했을 때의 cnt를 가지고 오지 못하고
# 그 수까지 cnt에 포함해서 나온 후 -1을 하게 되므로 논리적으로 일치하지는 않는다.

# while True:
#     if n < k:
#         break
#     target = (n // k) * k
#     cnt += n - target
#     n = target
#     n //= k
#     cnt += 1

# print(cnt)

# while True:
#     if n == 1: break
#     if n % k == 0:
#         n //= k
#         cnt += 1
#     else:
#         n -= 1
#         cnt += 1

# print(cnt)
