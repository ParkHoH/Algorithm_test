def chk_pelindrom(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False

    return True

N = int(input())
for _ in range(N):
    s = input()
    left = 0
    right = len(s) - 1
    semi_pelindrome = False
    nothing = False

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1

        elif not semi_pelindrome:
            if chk_pelindrom(s, left+1, right) or chk_pelindrom(s, left, right-1):
                semi_pelindrome = True
            else:
                nothing = True
            break

    if nothing:
        result = 2
    elif semi_pelindrome:
        result = 1
    else:
        result = 0

    print(result)

# eeeeea
# eeeaae
# abcba