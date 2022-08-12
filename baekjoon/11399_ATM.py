N = int(input())
P = list(map(int, input().split()))
P.sort()

sum = 0
result = 0
for i in P:
    sum += i
    result += sum

print(result)