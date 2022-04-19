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