from copy import deepcopy

def solution(board, aloc, bloc):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def find_way(a_x, a_y, b_x, b_y, cnt):
        if a_x == b_x and a_y == b_y:
            return

        min_distance = float('inf')
        for i in range(4):
            na_x = a_x + dx[i]
            na_y = a_y + dy[i]