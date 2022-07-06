def solution(money):
    dp_1 = [0] * len(money)
    dp_2 = [0] * len(money)
    dp_1[0], dp_2[0] = money[0], 0
    dp_1[1], dp_2[1] = max(money[0], money[1]), money[1]

    for i in range(2, len(money) - 1):
        dp_1[i] = max(dp_1[i-1], money[i] + dp_1[i-2])

    for i in range(2, len(money)):
        dp_2[i] = max(dp_2[i-1], money[i] + dp_2[i-2])

    return max(max(dp_1), max(dp_2))