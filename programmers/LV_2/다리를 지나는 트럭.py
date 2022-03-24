from collections import deque

def solution(bridge_length, weight, truck_weights):
    on_bridge = deque()
    truck_weights = deque(truck_weights)
    seconds = 0
    on_bridge_weight = 0
    
    # 대기 트럭이 빌 때까지 반복
    while truck_weights or on_bridge:
        seconds += 1

        # 해당 초에 완전히 지나간 트럭이 있으면 빼주기
        if len(on_bridge) > 0 and on_bridge[0][1] == seconds:
            pop_weight, _ = on_bridge.popleft()
            on_bridge_weight -= pop_weight
            
        # 대기하고 있는 트럭의 무게 + 현재 건너는 트럭의 무게가 weight 보다 작으면 새로운 트럭 올리기
        if len(truck_weights) > 0 and truck_weights[0] + on_bridge_weight <= weight:
            pop_weight = truck_weights.popleft()
            on_bridge_weight += pop_weight
            on_bridge.append([pop_weight, seconds+bridge_length])
            
    return seconds

print(solution(2,10,[7,4,5,6]))