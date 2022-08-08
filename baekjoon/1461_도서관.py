N, M = map(int, input().split())
L = list(map(int, input().split()))
L.sort()
minus = L[:]
plus = []

for i in range(N):
    if L[i] > 0:
        minus = L[:i]
        plus = L[i:][::-1]
        break

if N == len(minus):
    max_value = abs(minus[0])
elif N == len(plus):
    max_value = plus[0]
else:
    max_value = max(abs(minus[0]), plus[0])

result = -max_value

for i in range(0, len(minus), M):
    result += 2 * abs(minus[i])

for i in range(0, len(plus), M):
    result += 2 * plus[i]

print(result)

# 7 2
# [-39, -37, -29, -28, -6, 2, 11]
# 131

# 8 3
# [-45, -26, -18, -9, -4, 22, 40, 50]
# 158
