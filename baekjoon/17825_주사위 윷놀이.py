# 20까지는 원 바깥쪽
dice = list(map(int, input().split()))
direction = {i: [[i+j, 2*i + 2*j] for j in range(1, 6)] for i in range(21)} # 다음 인덱스, 가치

for i in range(1, 6):
    for j in range(1, i+1):
        direction[15+i][-j] = [-1, -1]

direction[5] = [[21, 13], [22, 16], [23, 19], [24, 25], [30, 30]]
direction[21] = [[22, 16], [23, 19], [24, 25], [30, 30], [31, 35]]
direction[22] = [[23, 19], [24, 25], [30, 30], [31, 35], [20, 40]]
direction[23] = [[24, 25], [30, 30], [31, 35], [20, 40], [-1, -1]]
direction[24] = [[30, 30], [31, 35], [20, 40], [-1, -1], [-1, -1]]

direction[10] = [[25, 22], [26, 24], [24, 25], [30, 30], [31, 35]]
direction[25] = [[26, 24], [24, 25], [30, 30], [31, 35], [20, 40]]
direction[26] = [[24, 25], [30, 30], [31, 35], [20, 40], [-1, -1]]

direction[15] = [[27, 28], [28, 27], [29, 26], [24, 25], [30, 30]]
direction[27] = [[28, 27], [29, 26], [24, 25], [30, 30], [31, 35]]
direction[28] = [[29, 26], [24, 25], [30, 30], [31, 35], [20, 40]]
direction[29] = [[24, 25], [30, 30], [31, 35], [20, 40], [-1, -1]]

direction[30] = [[31, 35], [20, 40], [-1, -1], [-1, -1], [-1, -1]]
direction[31] = [[20, 40], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]

def check_possible(idx):
    location = current[idx]

    for i in range(4):
        if idx == i:
            continue

        if location == current[i]:
            return False

    return True

def dfs(cnt, sum_value):
    if cnt == 10:
        global result
        result = max(result, sum_value)
        return

    for i in range(4):
        if current[i] == -1:
            continue

        new_idx = direction[current[i]][dice[cnt]-1][0]
        ori_idx = current[i]
        current[i] = new_idx

        if new_idx == -1:
            dfs(cnt+1, sum_value)
        elif check_possible(i):
            dfs(cnt+1, sum_value + direction[ori_idx][dice[cnt]-1][1])

        current[i] = ori_idx

result = 0
current = [dice[0], 0, 0, 0]

dfs(1, direction[0][dice[0]-1][1])

print(result)