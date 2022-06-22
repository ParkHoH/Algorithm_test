from copy import deepcopy

def dp(start, end, sticker):
    for i in range(start, end):
        if i == start:
            sticker[i] += sticker[i-2]
            continue
        sticker[i] += max(sticker[i-2], sticker[i-3])
        
    return max(sticker)

def solution(sticker):
    copy_sticker = deepcopy(sticker)
    if len(sticker) <= 3:
        return max(sticker)

    result = max(dp(2, len(sticker)-1, sticker), dp(3, len(copy_sticker), copy_sticker))
    return result

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))