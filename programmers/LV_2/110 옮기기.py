# stack을 이용한 풀이이지만 해당 문제의 시간 복잡도는 비효율적임
# 다른 풀이도 확인했으나 풀이가 모두 비슷한 것으로 보아 문제 오류로 보임
def solution(s):
    answer = []
    for string in s:
        stack = []
        cnt_110 = 0
        for str_i in string:
            if len(stack) >= 2 and stack[-1] == "1" and stack[-2] == "1" and str_i == "0":
                cnt_110 += 1
                stack.pop()
                stack.pop()
            else:
                stack.append(str_i)
        
        cnt_1 = 0
        for element in stack[::-1]:
            if element == "0":
                break
            else:
                cnt_1 += 1
                
        answer.append(''.join(stack[:len(stack)-cnt_1]) + "110"*cnt_110 + ''.join(stack[len(stack)-cnt_1:]))
    return answer


#my solution: 오답
def solution(s):
    result = []
    i = 0
    for string in s:
        cnt = 0
        while True:
            ori_len = len(string)
            string = ''.join(string.split("110"))
            cnt += (ori_len - len(string)) // 3
            if ori_len == len(string):
                break
        idx = string.find("111")
        if idx == -1:
            result.append("110"*cnt + string)
        else:
            result.append(string[:idx] + "110"*cnt + string[idx:])
    return result

print(solution(["1110","100111100","0111111010"]))