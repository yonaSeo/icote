import math


def is_prime_num(x):
    for i in range(2, int(math.sqrt(x)) + 1):  # 제곱근 포함한 범위(+1)까지 반복
        if x % i == 0:
            return False
        else:
            return True


print(is_prime_num(6))
print(is_prime_num(5))
