R, C = map(int, input().split())
board = [input() for _ in range(R)]
board = list(zip(*board))
start, end = 0, C-1

while start <= end:
    mid = (start + end) // 2
    case = set()

    for i in range(C):
        word = ''.join(board[i][mid:])
        possible = True

        if word in case:
            possible = False
            break

        case.add(word)

    if possible:
        start = mid+1
    else:
        end = mid-1

print(start-1)


# R, C = map(int, input().split())
# board = [list(input()) for _ in range(R)]
# start, end = 0, R-1

# while start <= end:
#     mid = (start + end) // 2
#     case = set()

#     for c in range(C):
#         word = ""
#         possible = True

#         for r in range(mid, R):
#             word += board[r][c]

#         if word in case:
#             possible = False
#             break

#         case.add(word)

#     if possible:
#         start = mid+1
#     else:
#         end = mid-1

# print(start-1)