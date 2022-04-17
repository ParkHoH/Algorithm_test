def solution(tickets):
    dic = {}
    for start, end in tickets:
        if start in dic:
            dic[start].append(end)
        else:
            dic[start] = [end]
    for key in dic.keys():
        dic[key].sort(reverse=True)
    
    answer = []
    stack = ["ICN"]
    while stack:
        airport = stack[-1]
        if airport in dic and dic[airport]:
            stack.append(dic[airport].pop())
        else:
            answer.append(stack.pop())
    return answer[::-1]

print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "ICN"]]))


# 2가지 TC 틀림
from collections import deque

def solution(tickets):
    # dictionary
    # key: 출발지 / value: [[도착지],0]
    dic = {}
    
    # tickets를 dictionary에 넣어줌
        # 있을 경우 value에 도착지만 append
        # 없을 경우 초기 세팅
    for start, end in tickets:
        if start in dic:
            dic[start][0].append(end)
        else:
            dic[start] = [[end], 0]
    
    for key, _ in dic.items():
        if len(dic[key][0]) > 1:
            dic[key][0].sort()
    
    result = []
    # BFS를 활용하기
    queue = deque()
    queue.append("ICN")
    while queue:
        start = queue.popleft()
        result.append(start)
        if start not in dic:
            break
        ends, idx = dic[start]
        if idx == len(ends):
            break
        queue.append(ends[idx])
        dic[start][1] += 1
        
    return result