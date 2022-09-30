# 전체 item의 개수 -> 이분 탐색을 통해 찾는다?
# 더 늦게 나오는 것을 제거함
from collections import defaultdict
from bisect import bisect_left

N, K = map(int, input().split())
items = list(map(int, input().split()))
dic = defaultdict(list)

for i, item in enumerate(items):
    dic[item].append(i)

multi_tap = set()
answer = 0

for i, item in enumerate(items):
    if item in multi_tap:
        continue

    if len(multi_tap) != N:
        multi_tap.add(item)
        continue
    
    candidate = [0, -1] # 가까운 순서, 인덱스

    for in_item in multi_tap:
        idxs = dic[in_item]
        temp = float('inf')

        searched_num = bisect_left(idxs, i)

        if searched_num == len(idxs):
            candidate[1] = in_item
            break

        distance = idxs[searched_num]

        if distance >= candidate[0]:
            candidate = [distance, in_item]

        # for idx in idxs:
        #     if idx >= i: 
        #         temp = idx
        #         break
        
        # if temp >= candidate[0]:
        #     candidate = [temp, in_item]

    answer += 1
    multi_tap.remove(candidate[1])
    multi_tap.add(item)

print(answer)