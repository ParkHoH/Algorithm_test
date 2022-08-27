import sys
input = sys.stdin.readline

def check():
    for i in range(n-1):
        if L[i] == L[i+1][:len(L[i])]:
            return False
    return True

T = int(input())

for _ in range(T):
    n = int(input())
    L = [input().rstrip() for _ in range(n)]

    L.sort()

    if check():
        print("YES")
    else:
        print("NO")