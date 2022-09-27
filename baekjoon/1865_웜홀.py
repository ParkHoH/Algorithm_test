from collections import defaultdict
import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = defaultdict(defaultdict(int))

    for _ in range(M):
        a, b, cost = map(int, input().split())
        