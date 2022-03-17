def solution(arr):
    result = [0, 0]
    def dfs(x, y, l):
        num = arr[x][y]
        for i in range(x, x+l):
            for j in range(y, y+l):
                if arr[i][j] != num:
                    l = l//2
                    dfs(x, y, l)
                    dfs(x, y+l, l)
                    dfs(x+l, y, l)
                    dfs(x+l, y+l, l)
                    return
        result[num] += 1
    
    dfs(0, 0, len(arr))
    return result

# print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))


# my solution: wrong
def solution(arr):
    dic = {0: 0, 1: 0}

    def dfs(start_x, start_y, end_x, end_y):
        num = arr[start_x][start_y]
        for i in range(start_x, end_x):
            for j in range(start_y, end_y):
                if arr[i][j] != num:
                    dfs(start_x, start_y, end_x//2, end_y//2)
                    dfs(start_x+end_x//2, start_y, end_x, end_y//2)
                    dfs(start_x, start_y+end_y//2, end_x//2, end_y)
                    dfs(start_x+end_x//2, start_y+end_y//2, end_x, end_y)
                    return
        dic[num] += 1

    dfs(0, 0, len(arr), len(arr))
    return dic

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))