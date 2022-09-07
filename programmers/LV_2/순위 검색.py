# 최근 풀이 (22. 09. 07)
from collections import defaultdict
from bisect import bisect_left

dict_info = defaultdict(list)

def subset(idx, combi, list_info):
    if idx == 4:
        dict_info[combi].append(int(list_info[-1]))
        return

    subset(idx+1, combi + list_info[idx], list_info)
    subset(idx+1, combi + "-", list_info)

def solution(info, query):
    for spec in info:
        subset(0, "", spec.split())

    for k, v in dict_info.items():
        dict_info[k] = sorted(v)

    result = []

    for q in query:
        q = q.split(" and ")
        q = q[:-1] + q[-1].split(" ")
        
        target = ''.join(q[:-1])
        score = int(q[-1])

        cnt = len(dict_info[target]) - bisect_left(dict_info[target], score)
        result.append(cnt)

    return result


from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    # 공백/and/- 제거
    info = [i.split() for i in info]
    query = [i.split(' and ') for i in query]
    for i in range(len(query)):
        food, score = query[i][3].split()
        query[i][3] = food
        query[i].append(score)
        while '-' in query[i]:
            query[i].remove('-')

    # 모든 info에 대해서 반복
    # info[:4]을 조합으로 표현
    # 해당 조합이 dic에 있으면 각 값에 info[4] append
    # dic에 없으면 새로 값 배열로 할당
    dic = {}
    for i in range(len(info)):
        for j in range(5):
            comb = list(combinations(info[i][:4], j))
            for c in comb:
                if c in dic:
                    dic[c].append(int(info[i][4]))
                else:
                    dic[c] = [int(info[i][4])]
    
    # dic 오름차순 정렬
    for key, value in dic.items():
        dic[key] = sorted(value)

    result = []
    for i in range(len(query)):
        if tuple(query[i][:-1]) in dic:
            cnt = bisect_left(dic[tuple(query[i][:-1])], int(query[i][-1]))
            result.append(len(dic[tuple(query[i][:-1])]) - cnt)
        else:
            result.append(0)
    return result