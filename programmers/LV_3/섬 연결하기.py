def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    connected = set()
    connected.update([costs[0][0], costs[0][1]])
    result = costs[0][2]
    
    while len(connected) != n:
        for cost in costs:
            if cost[0] in connected and cost[1] in connected:
                continue
            
            if cost[0] in connected or cost[1] in connected:
                result += cost[2]
                connected.update([cost[0], cost[1]])
                break
    
    return result

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))