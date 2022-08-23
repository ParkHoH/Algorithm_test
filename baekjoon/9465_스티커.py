import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    stickers = []
    for _ in range(2): # 2개 행으로 구분해 결과값 출력
        stickers.append(list(map(int, input().split())))

    if n == 1: # n이 1인 경우 바로 결과 출력
        print(max(stickers[0][0], stickers[1][0]))

    else:
        stickers[0][1] += stickers[1][0] # n이 2인 경우 결과값
        stickers[1][1] += stickers[0][0]

        for i in range(2, n): # n이 3인 경우
            stickers[0][i] += max(stickers[1][i-1], stickers[0][i-2], stickers[1][i-2])
            stickers[1][i] += max(stickers[0][i-1], stickers[0][i-2], stickers[1][i-2])

        print(max(stickers[0][-1], stickers[1][-1]))