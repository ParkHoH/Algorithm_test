def solution(prices):
    stack = [[prices[0], 0]]
    result = [0 for i in range(len(prices))]
    for i in range(1, len(prices)):
        while prices[i] < stack[-1][0]:
            pre_stack = stack.pop()
            result[pre_stack[1]] = i - pre_stack[1]
            if len(stack) == 0:
                break
        stack.append([prices[i], i])
    
    for i in range(len(result) - 1):
        if result[i] == 0:
            result[i] = len(result) - i - 1
    
    return result

print(solution([2, 1, 1, 1, 1, 2]))