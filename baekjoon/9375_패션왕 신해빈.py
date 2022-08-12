from collections import defaultdict
import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    n = int(input())
    dic = defaultdict(int)

    for _ in range(n):
        _, variety = input().split()
        dic[variety] += 1

    sum = 1
    for cnt in dic.values():
        sum *= (cnt+1)
    
    print(sum-1)
