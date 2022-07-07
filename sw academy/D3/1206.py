for case in range(1, 11):
    length = int(input())
    L = list(map(int, input().split()))
    dx = [-2, -1, 1, 2]

    result = 0
    for i in range(length):
        min_value = float('inf')
        for j in dx:
            if i+j < 0 or i+j >= length:
                continue

            if L[i+j] >= L[i]:
                min_value = 0
                break

            min_value = min(min_value, L[i] - L[i+j])
        
        if min_value: result += min_value

    print(f'#{case} {result}')