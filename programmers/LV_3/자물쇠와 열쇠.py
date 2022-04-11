def ratate_arr(ori_arr):
    n, m = len(ori_arr), len(ori_arr[0])
    new_arr = [[0] * n for _ in range(m)] 
    for i in range(n):
        for j in range(m):
            new_arr[j][n-i-1] = ori_arr[i][j]
    return new_arr

def solution(key, lock):
    for i in range(len(lock)):
        for j in range(len(lock[i])):
            lock[i][j] = 1 - lock[i][j]
            
    min_x = min_y = 20
    max_x = max_y = -1
    for y in range(len(lock)):
        for x in range(len(lock)):
            if lock[y][x] == 1:
                min_x, min_y = min(min_x, x), min(min_y, y)
                max_x, max_y = max(max_x, x), max(max_y, y)
    
    slice_lock = []
    for y in range(min_y, max_y+1):
        slice_lock.append(lock[y][min_x:max_x+1])

    for i in range(4):
        for start in range(len(key)):
            slice_key = key[start:start+len(slice_lock)]
            for x in range(len(key)):
                for y in range(len(slice_key)):
                    slice_key[y] = slice_key[y][x:x+len(slice_lock[0])]
                if slice_key == slice_lock:
                    return True
        slice_lock = ratate_arr(slice_lock)
    return False
    
print(solution(	[[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))