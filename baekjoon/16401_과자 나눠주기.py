# 문제가 조금 이상한 것 같음
# snack이 기본적으로 정렬되어 있지 않은데, 정답이 나오는 것은 이상하다.
M, N = map(int, input().split())
snacks = list(map(int, input().split()))

snacks.sort()

left, right = 0, snacks[-1]
result = 0

while left <= right:
    mid = (left + right) // 2

    if mid == 0:
        break

    cnt = 0
    for snack in snacks:
        cnt += snack // mid
        # if cnt >= M:
        #     break

    if cnt >= M:
        left = mid + 1
        result = mid
    else:
        right = mid - 1

print(result)