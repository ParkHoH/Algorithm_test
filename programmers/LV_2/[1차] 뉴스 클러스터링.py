import re
import math

def solution(str1, str2):
    str1, str2 = re.findall('[a-z]?', str1.lower()), re.findall('[a-z]?', str2.lower())
    L1, L2 = [], []
    for i in range(len(str1)-1):
        if str1[i] and str1[i+1]:
            L1.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if str2[i] and str2[i+1]:
            L2.append(str2[i]+str2[i+1])
            
    intersect = 0
    L2_copy = L2.copy()
    for i in L1:
        if i in L2_copy:
            intersect += 1
            L2_copy.remove(i)
    union = len(L1) + len(L2) - intersect
    
    if union:
        return math.floor((intersect / union) * 65536)
    else:
        return 65536