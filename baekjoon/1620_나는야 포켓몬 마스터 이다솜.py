import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}

for i in range(1, N+1):
    pocketmon = input().rstrip()
    dic[pocketmon] = i
    dic[str(i)] = pocketmon

for _ in range(M):
    question = input().rstrip()
    print(dic[question])