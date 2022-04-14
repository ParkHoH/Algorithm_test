def solution(gems):
    start = end = 0
    dic = {}
    cnt_gems = len(set(gems))
    result = [0, len(gems)-1]
    while end < len(gems):
        if gems[end] in dic:
            dic[gems[end]] += 1
        else:
            dic[gems[end]] = 1
        
        if len(dic) == cnt_gems:
            while start <= end:
                if dic[gems[start]] > 1:
                    dic[gems[start]] -= 1
                    start += 1
                else:
                    if end - start < result[1] - result[0]:
                        result = [start, end]
                    break
        end += 1
    return [result[0]+1, result[1]+1]