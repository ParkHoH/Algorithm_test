def solution(lottos, win_nums):
    correct_num = 6 - len(set(win_nums) - set(lottos))
    cnt = lottos.count(0)
    return [7 - (correct_num + cnt) if 7 - (correct_num + cnt) <= 6 else 6, 7 - correct_num if 7 - correct_num <= 6 else 6]