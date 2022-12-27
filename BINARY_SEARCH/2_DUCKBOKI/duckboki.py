n, m = map(int, input().split())
array = list(map(int, input().split()))

# 시작과 끝점 설정
start = 0
end = max(array)

result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m:  # 필요한 양보다 부족한 경우 떡 좀 더 많이 자르기 (왼쪽 부분 탐색)
        end = mid - 1
    else:  # 필요한 양보다 넘치거나 딱 맞는 경우 덜 자르기 (오른쪽 부분 탐색)
        result = mid  # 최대한 덜 잘랐을 때가 정답이므로 여기서 result에 기록한다.
        start = mid + 1

print(result)
