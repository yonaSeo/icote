array = [0] * 100
count = 0


def fibo(x):
    global count

    if x == 1 or x == 2:  # 종료 조건을 명시해준다.
        return 1

    if not array[x]:
        array[x] = fibo(x - 1) + fibo(x - 2)
        count += 1
        return array[x]
    else:
        return array[x]


print(fibo(99))
print(count)
