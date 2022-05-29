TC = int(input())
for case in range(1, TC+1):
    N = int(input())
    L = list(map(int, input().split()))

    sorted_L = sorted(L)
    result = 0
    while True:
        if sorted_L == L:
            print(f'#{case} {result}')
            break

        # 1번 과정
        for i in range(N-1):
            if i % 2 != 0:
                continue

            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
        
        # 2번 과정
        for i in range(1, N-1):
            if i % 2 == 0:
                continue

            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]

        result += 1