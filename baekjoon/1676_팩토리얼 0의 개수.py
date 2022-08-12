import math

N = int(input())
f = str(math.factorial(N))
cnt = 0

for s in f[::-1]:
    if s != "0":
        break
    cnt += 1

print(cnt)