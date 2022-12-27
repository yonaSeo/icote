n = int(input())
array = list(map(int, input().split()))

d = [0] * 100  # DP 테이블 초기화: 여기에 최적해가 누적된다.

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])  # 0번째 부터 계산했으므로 -1
