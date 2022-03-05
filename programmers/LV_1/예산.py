def solution(d, budget):
    d.sort()
    cnt = 0
    consum = 0
    
    for i in d:
        consum += i
        if consum > budget:
            continue
        cnt += 1
    
    return cnt


#better code
def solution(d, budget):
    d.sort()
    cnt = 0
    
    for i in d:
        budget -= i
        if budget < 0:
            continue
        cnt += 1
    
    return cnt