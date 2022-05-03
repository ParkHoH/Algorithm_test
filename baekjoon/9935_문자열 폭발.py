s = input()
bomb = input()
stack = []

for i in range(len(s)):
    stack.append(s[i])
    while True:
        if len(stack) >= len(bomb):
            if ''.join(stack[-len(bomb):]) == bomb:
                cnt = len(bomb)
                while cnt:
                    stack.pop()
                    cnt -= 1
            else:
                break
        else:
            break
        
if stack:
    print(''.join(stack))
else:
    print("FRULA")