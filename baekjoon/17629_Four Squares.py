n = int(input())
square = []

i = 1
while i**2 <= n:
    square.append(i**2)
    i += 1

result = 4

for i in range(len(square)-1, -1, -1):
    num1 = n
    num1 -= square[i]
    if num1 == 0:
        result = min(result, 1)
        break

    for j in range(i, -1, -1):
        if result <= 2:
            break

        num2 = num1
        num2 -= square[j]
        if num2 == 0:
            result = min(result, 2)
            break
        elif num2 < 0:
            continue

        for k in range(j, -1, -1):
            if result <= 3:
                break

            num3 = num2
            num3 -= square[k]
            if num3 == 0:
                result = min(result, 3)
                break
            elif num3 < 0:
                continue

print(result)