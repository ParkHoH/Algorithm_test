def dfs(queen, row, n):
    cnt = 0
    if n == row:
        return 1

    for col in range(n):
        queen[row] = col
        for i in range(row):
            if queen[i] == queen[row]:
                break
            if abs(queen[i]-queen[row]) == row - i:
                break
        else:
            cnt += dfs(queen, row + 1, n)
    return cnt

def solution(n):
    return dfs([0] * n, 0, n)