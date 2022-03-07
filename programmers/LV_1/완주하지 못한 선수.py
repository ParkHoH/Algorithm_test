#my solution
from collections import Counter
def solution(participant, completion):
    L = list(set(participant) - set(completion))
    Counter_part = Counter(participant).most_common()
    Counter_comp = Counter(completion).most_common()
    
    if len(L) == 1:
        return L[0]
    else:
        for key_part, value_part in Counter_part:
            for key_comp, value_comp in Counter_comp:
                if key_part == key_comp and value_part != value_comp:
                    return key_part


#better solution
from collections import Counter
def solution(participant, completion):
    L = Counter(participant) - Counter(completion)
    return list(L.keys())[0]


#hash function solution
def solution(participant, completion):
    dic = {}
    keys = 0
    for name in participant:
        dic[hash(name)] = name
        keys += hash(name)
    for name in completion:
        keys -= hash(name)
    return dic[keys]