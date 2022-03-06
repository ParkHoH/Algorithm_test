def solution(n, lost, reserve):
    lost, reserve = list(set(lost) - set(reserve)), list(set(reserve) - set(lost))
    
    for i in lost[:]:
        if i-1 in reserve:
            lost.remove(i)
            reserve.remove(i-1)
        elif i+1 in reserve:
            lost.remove(i)
            reserve.remove(i+1)
            
    return n - len(lost)

print(solution(7,[2, 3, 4],[1, 2, 3, 6]))