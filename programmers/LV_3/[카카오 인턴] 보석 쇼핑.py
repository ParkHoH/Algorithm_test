# 시간 초과: 투 포인터로 풀이 필요
def solution(gems):
    result = [1, len(gems)]
    set_gems = list(set(gems))
    if len(set_gems) == 1:
        return [1, 1]
    
    max_idx = 0
    reverse_gems = gems[::-1]
    for set_gem in set_gems:
        max_idx = max(reverse_gems.index(set_gem), max_idx)
        
    for i in range(len(gems)):
        if i == len(gems) - max_idx:
            break
        set_chk = set()
        set_chk.add((gems[i]))
        start, end = i, -1
        for j in range(i+1, len(gems)):
            if gems[i] == gems[j] or j-i >= result[1]-result[0]:
                break
            set_chk.add(gems[j])
            if len(set_chk) == len(set_gems):
                end = j
                break
        if end != -1 and end-start < result[1]-result[0]:
            result[0], result[1] = start+1, end+1
            if end-start == len(set_gems)-1:
                break
    return result

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))