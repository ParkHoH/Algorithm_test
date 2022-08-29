# 충전소와 N개의 집 사이 거리의 합이 최소

# 충전소는 최소한의 개수만 지어야 하며, 최대 2개까지 지을 수 있다.
# 만약 충전소를 1개만 지어도, 마을 내 모든 집에 전기 자동차를 보급할 수 있다면, 충전소는 반드시 1개만 지어야 한다.

# -----------------------
# 풀이
# 충전소 위치를 set에 담아줌 (house면 제외)
# 충전소에서 1개를 고르는 경우와 2개를 고르는 경우를 순처적으로 탐색
# 1개를 고를 경우 모든 집과 거리를 비교하고 집의 허용 거리보다 큰 경우 바로 탈출 -> 아닌 경우 답 갱신 (하나라도 있는 경우 2개 할 필요 없음)
# 2개를 고를 경우 모든 집과 두 좌표를 비교하고 집의 허용 거리보다 큰 경우 바로 탈출 

from itertools import combinations

def cal_dist(combi):
    sum_values = 0

    for i, j, dist in houses:
        distance = float('inf')
        for x, y in combi:
            distance = min(distance, abs(x - i) + abs(y - j))

        if distance > dist:
            return

        sum_values += distance

    global result
    result = min(result, sum_values)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    houses = [list(map(int, input().split())) for _ in range(N)]

    min_x = min_y = 15
    max_x = max_y = -15
    for i, j, d in houses:
        min_x = min(min_x, i-d)
        max_x = max(max_x, i+d)
        min_y = min(min_y, j-d)
        max_y = max(max_y, j+d)

    case = set()

    for i in range(max(-15, min_x), min(16, max_x+1)):
        for j in range(max(-15, min_y), min(16, max_y+1)):
            case.add((i, j))

    for i, j, _ in houses:
        case.remove((i, j))

    result = float('inf')

    for i in range(1, 3):
        for combi in combinations(case, i):
            cal_dist(combi)
        
        if result != float('inf'):
            break

    if result == float('inf'):
        result = -1
        
    print(f'#{tc} {result}')