n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)  # 모든 인덱스를 INF로 초기화
d[0] = 0

for i in range(n):
    for k in range(array[i], m + 1):
        if d[k - array[i]] != 10001:  # (i-k)원을 만드는 방법이 존재하는 경우
            d[k] = min(d[k], d[k - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
