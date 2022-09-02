N = int(input())
arr = list(map(int, input().split()))
len_list = [0] * N
stack = []

for i in range(N):
    standard = arr[i]

    if not stack or stack[-1] < standard:
        stack.append(standard)
        len_list[i] = len(stack)-1
    
    else:
        left, right = 0, len(stack)-1

        while left < right:
            mid = (left + right) // 2

            if stack[mid] < standard:
                left = mid + 1
            else:
                right = mid

        stack[right] = standard
        len_list[i] = right

result = []
idx = len(stack)-1

for i in range(N-1, -1, -1):
    if len_list[i] == idx:
        result.append(arr[i])
        idx -= 1

print(len(stack))
print(*result[::-1])