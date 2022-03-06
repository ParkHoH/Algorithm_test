#my solution
def solution(dartResult):
    i = 0
    result = []
    cnt = 0
    while len(dartResult) > i:
        score = 0
        
        #점수
        if dartResult[i+1].isdigit(): #10인 경우
            score = 10
            i += 2
        else:
            score = int(dartResult[i])
            i += 1
        
        #보너스
        if dartResult[i] == "D":
            score = score**2
        elif dartResult[i] == "T":
            score = score**3
        i += 1
        
        #옵션
        if len(dartResult) > i:
            if dartResult[i] == "*":
                if i < 4:
                    score = score*2
                else:
                    result[cnt-1] = result[cnt-1]*2
                    score = score*2
                i += 1
                    
            elif dartResult[i] == "#":
                score = 0 - score
                i += 1
        
        result.append(score)
        cnt += 1
        
    return sum(result)



#best solution: regular expression
import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

print(solution('10S2D*3T'))