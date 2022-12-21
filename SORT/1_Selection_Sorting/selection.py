array = [3, 0, 9, 2, 1, 8, 5, 7, 6, 4]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[min_index], array[i] = array[i], array[min_index]  # SWAP 연산

print(array)
