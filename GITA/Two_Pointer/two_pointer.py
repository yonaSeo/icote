n = 5  # 데이터의 개수
m = 5  # 찾고자 하는 부분합

data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0  # 부분합
end = 0

for start in range(n):  # start를 차례대로 증가시키며 반복
    while interval_sum < m and end < n:  # 부분합이 목표치에 못 치면
        interval_sum += data[end]  # end 포인터 + 1 이동
        end += 1

    if interval_sum == m:  # 부분합이 m일 때 카운트 증가
        count += 1

    # while문 빠져나왔단 건 부분합이 m보다 크거나 같다는 것이므로
    # 부분합의 start 포인터 + 1 이동
    interval_sum -= data[start]

print(count)
