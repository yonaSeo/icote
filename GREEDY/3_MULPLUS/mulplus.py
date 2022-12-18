data = input()
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

# s = input()
# result = 0

# for char in s:
#     n = int(char)
#     if n <= 1:
#         result += n
#     else:
#         if result <= 1:
#             result += n
#         else:
#             result *= n

# print(result)