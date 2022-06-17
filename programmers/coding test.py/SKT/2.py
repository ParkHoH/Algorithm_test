def chk_grade(period, amound_payed):
    # VIP - 이용기간: 2년 이상 ~ 5년 미만 / 누적액: 90만원 이상
    if 24 <= period < 60 and amound_payed >= 900000:
        grade = 'VIP'
    # VIP - 이용기간: 5년 이상 / 누적액: 60만원 이상
    elif period >= 60 and amound_payed >= 600000:
        grade = 'VIP'
    # 그 외 VIP 아님
    else:
        grade = 'normal'

    return grade

def solution(periods, payments, estimates):
    result = [0, 0]
    for i in range(len(periods)):
        # 이번 달 포함 이용 기간이 2년 미만인 경우 스킵
        if periods[i] + 1 < 24:
            continue
        
        # 현재 등급 구하기
        current_sum = sum(payments[i])
        current_grade = chk_grade(periods[i], current_sum)

        # 다음 등급 구하기
        after_sum = current_sum - payments[i][0] + estimates[i]
        after_grade = chk_grade(periods[i]+1, after_sum)

        # 등급 변경 시 결과에 추가
        if current_grade == 'normal' and after_grade == "VIP":
            result[0] += 1
        elif current_grade == 'VIP' and after_grade == "normal":
            result[1] += 1

    return result

print(solution([20, 23, 24], [[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]], [100000, 100000, 100000]))
print(solution([24, 59, 59, 60], [[50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]], [350000, 50000, 40000, 50000]))