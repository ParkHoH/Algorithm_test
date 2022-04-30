import sys

N, M = map(int, sys.stdin.readline().split())
dic = {}
for i in range(M):
    s_id = sys.stdin.readline().rstrip()
    dic[s_id] = i

answer = sorted(dic.items(), key=lambda x: x[1])
num = min(N, len(answer))
for i in range(num):
    print((answer[i][0]))