import heapq

TC = int(input())
for case in range(1, TC+1):
    heap = []
    print(f'#{case}', end=" ")

    for _ in range(int(input())):
        temp = list(map(int, input().split()))

        if temp[0] == 1:
            heapq.heappush(heap, -temp[1])
        elif heap:
            print(-heapq.heappop(heap), end=" ")
        else:
            print(-1, end=" ")

    print()