n = int(input())
length = len(str(n))
cnt = 0
result = ''
for i in range(length):
    result += str(n % 10 * (i+1))
    n = n // 10

print(result)