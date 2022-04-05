import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        else:
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
            cnt += 1
    return cnt


# 시간 초과
def solution(scoville, K):
    cnt = 0
    scoville.sort(reverse=True)
    while scoville[-1] < K:
        if len(scoville) == 1:
            return -1
        else:
            a = scoville.pop()
            b = scoville.pop()
            scoville.append(a+b*2)
            scoville.sort(reverse=True)
            cnt += 1
    return cnt