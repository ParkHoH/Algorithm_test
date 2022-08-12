import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}

for i in range(N):
    string = input().rstrip()
    dic[string] = 1

result = []
for i in range(M):
    string = input().rstrip()
    if string in dic:
        result.append(string)

result.sort()

print(len(result))
for i in result:
    print(i)