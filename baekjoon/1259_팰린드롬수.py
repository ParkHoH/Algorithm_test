while True:
    num = input()
    if num == "0":
        break

    left = 0
    right = len(num)-1
    pelindrom = True

    while left < right:
        if num[left] != num[right]:
            pelindrom = False
            break

        left += 1
        right -= 1

    if pelindrom:
        print("yes")
    else:
        print("no")