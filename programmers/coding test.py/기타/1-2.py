def solution(n, clockwise):
    L = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(4):
        num = n-1
        cnt = 0
        if clockwise == True:
            if i == 0:
                dx, dy = -1, 0
                flag = "x_plus"
            elif i == 1:
                dx, dy = num, -1
                flag = "y_plus"
            elif i == 2:
                dx, dy = n, num
                flag = "x_minus"
            elif i == 3:
                dx, dy = 0, n
                flag = "y_minus"
        elif clockwise == False:
            if i == 0:
                dx, dy = 0, -1
                flag = "y_plus"
            elif i == 1:
                dx, dy = n, 0
                flag = "x_minus"
            elif i == 2:
                dx, dy = num, n
                flag = "y_minus"
            elif i == 3:
                dx, dy = -1, num
                flag = "x_plus"

        while num > 1:
            for _ in range(num):
                if flag == "x_plus":
                    dx += 1
                elif flag == "x_minus":
                    dx -= 1
                elif flag == "y_plus":
                    dy += 1
                elif flag == "y_minus":
                    dy -= 1
                cnt += 1
                L[dy][dx] = cnt

            if clockwise == True:
                if flag == "x_plus":
                    flag = "y_plus"
                elif flag == "y_plus":
                    flag = "x_minus"
                elif flag == "x_minus":
                    flag = "y_minus"
                elif flag == "y_minus":
                    flag = "x_plus"
            elif clockwise == False:
                if flag == "x_plus":
                    flag = "y_minus"
                elif flag == "y_minus":
                    flag = "x_minus"
                elif flag == "x_minus":
                    flag = "y_plus"
                elif flag == "y_plus":
                    flag = "x_plus"
            
            num -= 2

    if n % 2 == 0:
        L[n//2 - 1][n//2 - 1] = cnt + 1
        L[n//2 - 1][n//2] = cnt + 1
        L[n//2][n//2 -1] = cnt + 1
        L[n//2][n//2] = cnt + 1
    else:
        L[n//2][n//2] = cnt + 1

    return L

print(solution(5, True))
print(solution(6, False))