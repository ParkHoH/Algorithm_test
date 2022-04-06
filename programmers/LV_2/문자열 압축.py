def solution(s):
    max_comp = int(len(s)//2) + 1
    result = []
    for comp_len in range(1, max_comp+1):
        comp_s = ''
        i = 0
        while i < len(s):
            cnt = 1
            while s[i:i+comp_len] == s[i+comp_len:i+2*comp_len]:
                i += comp_len
                cnt += 1
            else:
                if cnt == 1:
                    comp_s += s[i:i+comp_len]
                else:
                    comp_s += str(cnt) + s[i:i+comp_len]
                i += comp_len
        
        result.append(len(comp_s))
    return min(result)
            
print(solution("xababcdcdababcdcd"))