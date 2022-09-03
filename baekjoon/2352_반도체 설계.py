n = int(input())
ports = list(map(int, input().split()))

stack = []

for port in ports:
    if not stack or stack[-1] < port:
        stack.append(port)

    else:
        left, right = 0, len(stack)-1

        while left < right:
            mid = (left + right) // 2

            if stack[mid] < port:
                left = mid + 1
            else:
                right = mid

        stack[right] = port

print(len(stack))