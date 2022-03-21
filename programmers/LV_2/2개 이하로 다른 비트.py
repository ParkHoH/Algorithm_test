# other solution
def solution(numbers):
    result = []
    numbers = list(map(int, numbers))
    for number in numbers:
        if number % 2 == 0:
            result.append(number+1)
            continue
        else:
            bin_number = '0' + bin(number)[2:]
            idx = bin_number.rfind('0')
            bin_number = list(bin_number)
            bin_number[idx] = '1'
            bin_number[idx+1] = '0'
            result.append(int(''.join(bin_number), 2))
    return result


# 시간 초과이지만 비트연산자를 통해 해결한 solution
def solution(numbers):
    result = []
    numbers = list(map(int, numbers))
    for number in numbers:
        n = number + 1
        while True:
            if bin(n^number).count('1') <= 2:
                result.append(n)
                break
            n += 1
    return result


# my solution: wrong
def solution(numbers):
    dic = {}
    answer = []
    for number in numbers:
        rst = number + 1
        bin_number = bin(number)[2:]
        if bin_number not in dic:
            dic[number] = bin_number
        while True:
            ori_num = bin_number
            if rst in dic:
                rst = dic[rst] # string
            else:
                bin_rst = bin(rst)[2:] # string
                dic[rst] = bin_rst

            length = len(bin_rst)
            ori_num = ori_num.rjust(length, '0')
            cnt = 0
            for i in range(length):
                if bin_rst[i] != ori_num[i]:
                    cnt += 1
            if 1 <= cnt <= 2:
                answer.append(rst)
                break
            rst += 1
    return answer

print(solution([2,7]))