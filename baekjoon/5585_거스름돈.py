n = 1000 - int(input())
result = 0

for i in [500, 100, 50, 10, 5, 1]:
    result += n // i
    n %= i

print(result)