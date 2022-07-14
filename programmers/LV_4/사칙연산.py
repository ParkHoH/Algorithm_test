def solution(arr):
    result = [0, 0]
    sum_value = 0
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == "+":
            continue

        elif arr[i] == "-":
            min, max = result
            result[0] = min(-(sum_value + max), -sum_value + min)
            minus_v = int(arr[i+1])
            result[1] = max(-(sum_value+min), -minus_v+(sum_value-  minus_v) + max)
            sum_value = 0

        elif int(arr[i]) >= 0:
            sum_value += int(arr[i])

    result[1] += sum_value
    return result[1]