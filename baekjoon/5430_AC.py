import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    alphabets = list(input().rstrip())
    n = int(input().rstrip())
    L = input().rstrip()[1:-1].split(",")

    if n == 0:
        if "D" in alphabets:
            print("error")
        else:
            print("[]")
        continue

    reverse = False
    stop = False
    right = n-1
    left = 0
    
    for s in alphabets:
        if s == "R":
            reverse = not reverse

        elif s == "D":
            if left > right:
                stop = True
                break

            if reverse:
                right -= 1
            else:
                left += 1

    if stop:
        print("error")
    else:
        if reverse:
            print("[" + ','.join(L[left:right+1][::-1]) + "]")
        else:
            print("[" + ','.join(L[left:right+1]) + "]")