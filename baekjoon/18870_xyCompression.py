import sys
from collections import Counter

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

result_L = sorted(list(set(L)))

#dictionay key, value 할당 방법 1
dic = {}
for i in range(len(result_L)):
    dic[result_L[i]] = i

#dictionay key, value 할당 방법 2
dic = {result_L[i] : i for i in range(len(result_L))}


for i in L:
    print(dic[i], end=' ')