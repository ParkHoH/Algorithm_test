from itertools import combinations

def solution(orders, course):
    # orders 뽑을 때 정렬하기
    # dictionary 에 조합을 이용해서 course 만큼 개수 세고 넣어주기
    dic = {}
    for num in course:
        for order in orders:
            for comb in list(combinations(sorted(order), num)):
                comb = ''.join(comb)
                dic[comb] = dic[comb] + 1 if comb in dic else 1
    
    # course 만큼 for문 돌면서 dictionary 에 해당 최대값을 구하고, 최대값과 일치하면 result 에 넣어주기
    result = []
    for num in course:
        max_value = 0
        for key, value in dic.items():
            if len(key) == num and value > max_value:
                max_value = value
        if max_value >= 2:
            for key, value in dic.items():
                if len(key) == num and value == max_value:
                    result.append(key)
    
    # result 정렬해서 넣기
    result.sort()
    return result


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))