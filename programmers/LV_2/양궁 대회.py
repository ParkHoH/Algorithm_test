from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    max_score = 0
    for comb in combinations_with_replacement(range(11), n):
        dic_lion = Counter(comb)
        score_lion, score_apichi = 0, 0
        for num in range(10):
            score = 10 - num
            if info[num] > dic_lion[score]:
                score_apichi += score
            elif info[num] < dic_lion[score]:
                score_lion += score
            elif info[num] != 0:
                score_apichi += score
                
        if score_lion - score_apichi > max_score:
            max_score = score_lion - score_apichi
            max_arr = dic_lion
            
    if max_score == 0:
        return [-1]
    else:
        return [max_arr[i] for i in range(10, -1, -1)]


# dfs solution
from copy import deepcopy

def solution(n, info):
    max_arr = [0, []]
    def dfs(i, cnt, score_aphichi, score_lion, board):
        if i > 10:
            board[10] = n - cnt
            if score_lion - score_aphichi > max_arr[0]:
                max_arr[0] = score_lion - score_aphichi
                max_arr[1] = board

            elif max_arr[0] and score_lion - score_aphichi == max_arr[0]:
                change = False
                for i in range(10, -1, -1):
                    if max_arr[1][i] > board[i]:
                        break
                    elif max_arr[1][i] < board[i]:
                        change = True
                        break
                if change:
                    max_arr[1] = board            
                
            return

        required_cnt = info[i] + 1
        if cnt + required_cnt <= n:
            copy_board = deepcopy(board)
            copy_board[i] = required_cnt
            dfs(i+1, cnt+required_cnt, score_aphichi, score_lion+(10-i), copy_board)

        if info[i]:
            dfs(i+1, cnt, score_aphichi+(10-i), score_lion, board)
        else:
            dfs(i+1, cnt, score_aphichi, score_lion, board)

    board = [0] * 11
    dfs(0, 0, 0, 0, board)

    if max_arr[1]:
        return max_arr[1]
    else:
        return [-1]


print(solution(	5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))