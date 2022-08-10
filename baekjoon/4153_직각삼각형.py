while True:
    L = list(map(int, input().split()))

    if L[0] == L[1] == L[2] == 0:
        break

    num1 = num2 = 0
    for i in L:
        if i == max(L):
            num1 += i ** 2
        else:
            num2 += i ** 2

    if num1 == num2:
        print("right")
    else:
        print("wrong")