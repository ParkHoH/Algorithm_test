import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))
B, C = map(int, input().split())
result = 0

for i in L:
    if i > B:
        cnt = (i-B) // C
        if (i-B) % C:
            cnt += 1
        result += cnt + 1
    else:
        result += 1

print(result)