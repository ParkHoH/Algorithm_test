def solution(id_list, report, k):
    report = [i.split() for i in set(report)]
    dic = {name: [0, 0] for name in id_list} #[신고 당한 횟수, 메일 횟수]
    
    for i in report:
        dic[i[1]][0] +=  1
        
    for i in report:
        if dic[i[1]][0] >= k:
            dic[i[0]][1] += 1
    
    return [i[1] for i in dic.values()]