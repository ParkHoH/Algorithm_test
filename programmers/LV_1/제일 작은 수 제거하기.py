def solution(arr):
    arr_min = min(arr)
    arr.remove(arr_min)
    
    if len(arr) < 2:
        return [-1]
    return arr

#short code
def solution(arr):
    arr.remove(min(arr))
    
    return [-1] if len(arr) < 2 else arr