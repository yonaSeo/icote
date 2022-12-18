n = int(input())
result = 0

# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#                 if '3' in str(i) + str(j) + str(k):
#                     result += 1

# print(result)

nums = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            for num in nums:
                if i == num or j == num or k == num:
                    result += 1
                    break;

print(result)