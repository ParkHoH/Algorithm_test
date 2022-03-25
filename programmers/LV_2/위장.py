from itertools import combinations

def solution(clothes):
    dic = {}
    for cloth in clothes:
        if cloth[1] in dic:
            dic[cloth[1]] += 1
        else:
            dic[cloth[1]] = 1
            
    result = len(clothes)
    for i in range(2, len(dic)+1):
        c = list(combinations(dic.values(), i))
        for num_arr in c:
            multiflied_value = 1
            for num in num_arr:
                multiflied_value *= num
            result += multiflied_value
            
    return result

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))