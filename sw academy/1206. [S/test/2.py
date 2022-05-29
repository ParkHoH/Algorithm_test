from copy import deepcopy

TC = int(input())
for case in range(1, TC+1):
    N = int(input())
    dic = {}
    checked = [False] * (N+1)
    checked_cnt = 0

    for i in range(1, N+1):
        L = list(map(int, input().split()))
        if len(L) == 1:
            checked[i] = True
            checked_cnt += 1
            continue
        dic[i] = L[1:]

    result = 1
    while True:
        if checked_cnt == N:
            print(f'#{case} {result}')
            break

        stop = True
        copy_checked = deepcopy(checked)
        for i in range(1, N+1):
            if checked[i]:
                continue

            skip = False
            for idx in dic[i]:
                if not checked[idx]:
                    skip = True
                    break
            
            if skip:
                continue
            
            copy_checked[i] = True
            checked_cnt += 1
            stop = False

        if stop:
            print(f'#{case} {-1}')
            break

        checked = copy_checked
        result += 1