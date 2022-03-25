# my solution
def solution(s):
    s = s[2:-2]
    s = list(map(str, s.split('},{')))
    s.sort(key=lambda x: len(x))
    dic = {}
    result = []
    for i in s:
        L = i.split(',')
        for j in L:
            if j not in dic:
                dic[j] = 0
                result.append(int(j))
    return result

# other's solution
from collections import Counter
import re

def solution(s):
    s = Counter(re.findall('\d+', s))
    s = sorted(s.items(), key=lambda x: x[1], reverse=True)
    result = [int(item[0]) for item in s]
    return result