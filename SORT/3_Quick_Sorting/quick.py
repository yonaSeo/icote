array = [3, 0, 9, 2, 1, 8, 5, 7, 6, 4]


def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # pivot 보다 큰 left 찾을 때까지
        # while arr[left] <= arr[pivot] and left <= end: -> 이렇게 해버리면 arr에 초과 인덱스 담겨서 에러난다!
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # pivot 보다 작은 right 찾을 때까지
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:  # 엇갈렸으면 pivot right 스왑
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:  # 엇갈리지 않았으면 left right 스왑
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right - 1)  # 현재 right이 pivot이므로 -1이 end
    quick_sort(arr, right + 1, end)  # 현재 right이 pivot이므로 +1이 start


quick_sort(array, 0, len(array) - 1)
print(array)
