L = list(map(int, input().split()))
num = 0
for i in range(len(L)):
    num += L[i] ** 2

print(num % 10)