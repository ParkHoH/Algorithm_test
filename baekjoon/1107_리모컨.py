N = int(input())
M = int(input())

if M == 0:
    broken = []
else:
    broken = input().split()
dic = {}

for b in broken:
    dic[b] = 1

result = abs(N-100)
for i in range(1000001):
    impossible = False

    for j in set(str(i)):
        if j in dic:
            impossible = True
            break

    if not impossible:
        result = min(result, abs(N-i) + len(str(i)))

    if result == 0:
        break

print(result)