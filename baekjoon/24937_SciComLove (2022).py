N = int(input())
N %= 10
s = "SciComLove"

for _ in range(N):
    s = s[1:] + s[0]

print(s)