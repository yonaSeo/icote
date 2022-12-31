import heapq


def heap_sort(iterable):  # 오름차 순 힙 정렬(Heap Sort)
    h = []
    result = []
    for value in iterable:  # 모든 원소 차례대로 힙에 삽입
        heapq.heappush(h, value)  # 내림차 순일 때 : -value
    for i in range(len(h)):  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
        result.append(heapq.heappop(h))  # 내림차 순일 때 : -heapq.heappop(h)
    return result


result = heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
