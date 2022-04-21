def solution(stones, k):
    start, end = 0, len(stones)
    while start <= end:
        mid = (start+end) // 2
        impossible = 0
        for stone in stones:
            if stone <= mid:
                impossible += 1
            else:
                impossible = 0
            if impossible >= k:
                break
        if impossible >= k:
            end = mid
        else:
            start = mid + 1
    return start

# my solution: 시간 초과
def solution(stones, k):
    max_value = float('inf')
    for i in range(len(stones)-k+1):
        if stones[i] >= max_value:
            continue
        temp = max(stones[i:i+k])
        if temp < max_value:
            max_value = temp
    return max_value

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))