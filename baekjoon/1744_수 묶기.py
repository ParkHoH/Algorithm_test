N = int(input())
L = [int(input()) for _ in range(N)]

L.sort()
minus, one, plus = [], [], []

for i in L:
    if i <= 0:
        minus.append(i)
    elif i == 1:
        one.append(i)
    else:
        plus.append(i)

def check(arr):
    sum = 0

    for i in range(0, len(arr), 2):
        if i == len(arr)-1:
            sum += arr[i]
        else:
            sum += arr[i] * arr[i+1]

    return sum

result = check(minus) + sum(one) + check(plus[::-1])
print(result)