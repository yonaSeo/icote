import math

n = 1000

# 처음에는 모든 수가 소수(True)인 것으로 초기화
array = [True for _ in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):  # 2부터 n 제곱근 범위 중
    if array[i] == True:  # i가 소수인 경우
        j = 2
        while i * j <= n:  # i를 제외한 i의 모든 배수 지우기
            array[i * j] = False
            j += 1

for i in range(2, n + 1):
    if array[i]:
        print(i, end=" ")
