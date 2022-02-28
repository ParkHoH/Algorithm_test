N = int(input())
result = 0

for i in range(1, N+1):
    temp = i
    for j in range(len(str(i))):
        temp += int(str(i)[j])
    if temp == N:
        result = i
        break

print(result)