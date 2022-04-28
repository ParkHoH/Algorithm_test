from itertools import permutations
from collections import deque
from copy import deepcopy

def solution(board, r, c):
    dic = {}
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                if board[i][j] in dic:
                    dic[board[i][j]].append([i, j])
                else:
                    dic[board[i][j]] = [[i, j]]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    direction = ["r_direction", "c_direction"]

    def bfs(r, c, target_r, target_c, copy_board):
        list_distance = [[float('inf')] * 4 for _ in range(4)]
        list_distance[r][c] = 0
        queue = deque()
        queue.append((r, c, 0, ""))
        set_rc = set()
        while queue:
            r, c, distance, d = queue.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                direct = direction[i//2]
                if nr >= 4 or nc >= 4 or nr < 0 or nc < 0:
                    continue

                if direct == d:
                    if copy_board[r][c] == 0:
                        dist = distance
                    else:
                        dist = distance + 1
                else:
                    dist = distance + 1

                if dist < list_distance[nr][nc]:
                    list_distance[nr][nc] = dist
                    queue.append((nr, nc, dist, direct))
                    set_rc.add((r, c, nr, nc))
                elif dist == list_distance[nr][nc] and (r, c, nr, nc) not in set_rc:
                    list_distance[nr][nc] = dist
                    queue.append((nr, nc, dist, direct))
                    set_rc.add((r, c, nr, nc))
        
        return list_distance[target_r][target_c]

    answer = []
    for comb in permutations(permutations(dic.keys(), 2), len(dic.keys())):
        result = 0
        copy_board = deepcopy(board)
        copy_r, copy_c = r, c
        for i in range(len(comb)):
            r_1, c_1 = dic[comb[i]][0]
            r_2, c_2 = dic[comb[i]][1]
            case_1 = bfs(copy_r, copy_c, r_1, c_1, copy_board) + bfs(r_1, c_1, r_2, c_2, copy_board)
            case_2 = bfs(copy_r, copy_c, r_2, c_2, copy_board) + bfs(r_2, c_2, r_1, c_1, copy_board)
            copy_board[r_1][c_1] = 0
            copy_board[r_2][c_2] = 0

            if case_1 <= case_2:
                result += case_1 + 2
                copy_r, copy_c = r_2, c_2
            elif case_1 > case_2:
                result += case_2 + 2
                copy_r, copy_c = r_1, c_1
            # else:
            #     result += case_2 + 2
            #     if i != len(comb)-1:
            #         cnt1_1 = bfs(r_2, c_2, dic[comb[i]][0][0], dic[comb[i]][0][1], copy_board) + bfs(dic[comb[i]][0][0], dic[comb[i]][0][1], dic[comb[i]][1][0], dic[comb[i]][1][1], copy_board)
            #         cnt1_2 = bfs(r_2, c_2, dic[comb[i]][1][0], dic[comb[i]][1][1], copy_board) + bfs(dic[comb[i]][1][0], dic[comb[i]][1][1], dic[comb[i]][0][0], dic[comb[i]][0][1], copy_board)
            #         cnt2_1 = bfs(r_1, c_1, dic[comb[i]][0][0], dic[comb[i]][0][1], copy_board) + bfs(dic[comb[i]][0][0], dic[comb[i]][0][1], dic[comb[i]][1][0], dic[comb[i]][1][1], copy_board)
            #         cnt2_2 = bfs(r_1, c_1, dic[comb[i]][1][0], dic[comb[i]][1][1], copy_board) + bfs(dic[comb[i]][1][0], dic[comb[i]][1][1], dic[comb[i]][0][0], dic[comb[i]][0][1], copy_board)
            #         if min(cnt1_1, cnt1_2) <= min(cnt2_1, cnt2_2):
            #             copy_r, copy_c = r_1, c_1
            #         else:
            #             copy_r, copy_c = r_2, c_2

        answer.append(result)

    return min(answer)

print(solution(	[[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))