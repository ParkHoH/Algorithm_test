def solution(s):
    cnt = cnt_zero = 0
    while s != '1':
        cnt_one = s.count('1')
        cnt += 1
        cnt_zero += len(s) - cnt_one
        s = bin(int(cnt_one))[2:]
    return [cnt, cnt_zero]

print(solution("1111111"))