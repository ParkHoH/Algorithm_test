from collections import deque, defaultdict

TC = int(input())
for _ in range(TC):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))

    important = sorted(list(set(L)))
    dic = defaultdict(int)
    queue = deque()

    for i in range(len(L)):
        dic[L[i]] += 1
        queue.append([L[i], i])

    result = 0
    while queue:
        num, i = queue.popleft()

        if num == important[-1]:
            result += 1
            dic[num] -= 1

            if i == M:
                break
            if dic[num] == 0:
                important.pop()

        else:
            queue.append([num, i])

    print(result)