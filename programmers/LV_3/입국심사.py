def solution(stones, k):
    start, end = 0, 200000000
    while start < end: # '<='도 가능하지만 end = mid-1 로 변경해줘야 함
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


# 시간 초과
import heapq

def solution(n, times):
    cnt = result = 0
    time_heaq = []
    for time in times:
        heapq.heappush(time_heaq, (time, time))
    while cnt != n:
        time_complited, time_cost = heapq.heappop(time_heaq)
        heapq.heappush(time_heaq, (time_complited+time_cost, time_cost))
        cnt += 1
        result = time_complited
    return result

print(solution(6,[10, 7]))