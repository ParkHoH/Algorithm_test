def solution(arr):
    i = 2
    while True:
        cnt = 0
        for n in arr:
            cnt += 1 if i % n == 0 else cnt
        if cnt == len(arr):
            return i
        i += 1