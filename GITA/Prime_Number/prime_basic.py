def is_prime_num(x):
    for i in range(2, x):  # 2부터 x-1까지
        if x % i == 0:
            return False
        else:
            return True


print(is_prime_num(5))
print(is_prime_num(6))
