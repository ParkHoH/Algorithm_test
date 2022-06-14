from copy import deepcopy

TC = int(input())
for case in range(1, TC+1):
    # 수업 수
    N = int(input())
    dic = {}
    checked = [False] * (N+1)
    checked_cnt = 0

    # 딕셔너리: 수업 번호에 따른 선행 수업 번호
    for i in range(1, N+1):
        L = list(map(int, input().split()))
        if len(L) == 1:
            checked[i] = True
            checked_cnt += 1
            continue
        dic[i] = L[1:]
    
    result = 1
    # 수업을 다 들을 때까지 반복
    while True:
        # 모든 수업을 들은 경우 결과 출력 후 break
        if checked_cnt == N:
            print(f'#{case} {result}')
            break

        stop = True
        copy_checked = deepcopy(checked)
        # 1번 수업부터 N번 수업까지 하나씩 체크
        for i in range(1, N+1):
            # 이미 들은 경우 스킵
            if checked[i]:
                continue
            
            skip = False
            # 선행 수업을 하나씩 체크
            for idx in dic[i]:
                # 선행 수업을 아직 듣지 않은 경우 스킵
                if not checked[idx]:
                    skip = True
                    break
            
            if skip:
                continue
            
            copy_checked[i] = True
            checked_cnt += 1
            stop = False

        # 모든 수업 수강이 불가능한 경우 -1 출력
        if stop:
            print(f'#{case} {-1}')
            break

        checked = copy_checked
        result += 1