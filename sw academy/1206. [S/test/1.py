TC = int(input())
for case in range(1, TC+1):
    N = int(input())
    L = list(map(int, input().split()))

    # sorted_L: 최종 정렬된 리스트
    sorted_L = sorted(L)
    result = 0
    while True:
        # 과정을 끝낸 리스트가 최종 정렬된 리스트와 같은 경우 break
        if sorted_L == L:
            print(f'#{case} {result}')
            break

        # 1번 과정
        for i in range(N-1):
            # 홀수인 경우 스킵
            if i % 2 != 0:
                continue

            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
        
        # 2번 과정
        for i in range(1, N-1):
            # 짝수인 경우 스킵
            if i % 2 == 0:
                continue

            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]

        result += 1