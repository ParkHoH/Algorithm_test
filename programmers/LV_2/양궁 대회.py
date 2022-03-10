from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    max_score = 0
    for comb in combinations_with_replacement(range(11), n):
        dic_lion = Counter(comb)
        score_lion, score_apichi = 0, 0
        for num in range(10):
            score = 10 - num
            if info[num] > dic_lion[score]:
                score_apichi += score
            elif info[num] < dic_lion[score]:
                score_lion += score
            elif info[num] != 0:
                score_apichi += score
                
        if score_lion - score_apichi > max_score:
            max_score = score_lion - score_apichi
            max_arr = dic_lion
            
    if max_score == 0:
        return [-1]
    else:
        return [max_arr[i] for i in range(10, -1, -1)]