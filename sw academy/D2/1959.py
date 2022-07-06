def findFunction(arr_1, arr_2):
    n = len(arr_1) - len(arr_2)
    result = -float('inf')
    for i in range(n + 1):
        num = 0
        for j in range(len(arr_2)):
            num += arr_1[i + j] * arr_2[j]
        
        result = max(result, num)

    return result

TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N >= M:
        result = findFunction(A, B)
    else:
        result = findFunction(B, A)

    print(f'#{tc} {result}')