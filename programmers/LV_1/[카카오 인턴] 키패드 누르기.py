def solution(numbers, hand):
    answer = ''
    L_land = [3, 0]
    R_land = [3, 2]
    
    for number in numbers:
        if number == 0:
            x, y = 3, 1
        else:
            x, y = (number-1) // 3, (number-1) % 3
            
        if y == 0: #왼쪽 키패드
            L_land = [x, y]
            answer += "L"
        elif y == 2: #오른쪽 키패드
            R_land = [x, y]
            answer += "R"
        else: #중간 키패드
            if abs(x - L_land[0]) + abs(y - L_land[1]) < abs(x - R_land[0]) + abs(y - R_land[1]): #왼손 가까운 경우
                L_land = [x, y]
                answer += "L"
            elif abs(x - L_land[0]) + abs(y - L_land[1]) > abs(x - R_land[0]) + abs(y - R_land[1]): #오른손 가까운 경우
                R_land = [x, y]
                answer += "R"
            else: #거리 같은 경우
                if hand == "left":
                    L_land = [x, y]
                    answer += "L"
                else:
                    R_land = [x, y]
                    answer += "R"
    return answer