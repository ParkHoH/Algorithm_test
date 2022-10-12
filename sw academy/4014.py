TC = int(input())

for tc in range(1, TC+1):
    N, X = map(int, input().split())
    board = [[*map(int, input().split())] for _ in range(N)]
    answer = 0

    def check(L):
        previous_cnt = 1
        x = 0

        for i in range(N-1):
            diff = L[i] - L[i+1]

            if diff == 0:
                previous_cnt += 1
                if x != 0: 
                    x -= 1
                    previous_cnt = 0

            elif diff == 1:
                if x != 0:
                    return False
                x = X-1
                previous_cnt = 0

            elif diff == -1:
                if previous_cnt < X:
                    return False

                
                previous_cnt = 1
                x = 0

            else:
                return False
        
        return True if x == 0 else False


    for i in range(N):
        answer += check(board[i])
    
    for j in range(N):
        L = []
        for i in range(N):
            L += [board[i][j]]
        
        answer += check(L)

    print(f"#{tc} {answer}")