array = [3, 0, 9, 2, 1, 8, 5, 7, 6, 4]

for i in range(1, len(array)):
    for j in range(i, 0, -1):  # 인덱스 1부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j - 1]:  # 한 칸씩 왼쪽으로 이동: 부등호 방향이 바뀌면 내림차 정렬이 된다.
            array[j], array[j - 1] = array[j - 1], array[j]
        else:  # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
