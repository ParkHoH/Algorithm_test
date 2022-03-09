def solution(msg):
    dic = {chr(i + 64) : i for i in range(1, 27)}
    answer = []
    while len(msg) > 0:
        for i in range(len(msg)):
            stop = False
            for j in range(len(msg)-1, i, -1):
                if msg[i:j+1] in dic:
                    answer.append(dic[msg[i:j+1]])
                    dic[msg[i:j+2]] = len(dic) + 1
                    msg = msg[j+1:]
                    stop = True
                    break
            if stop:
                break
            answer.append(dic[msg[i]])
            dic[msg[i:i+2]] = len(dic) + 1
            msg = msg[i+1:]
            break
    return answer


#better solution
def solution(msg):
    dic = {chr(i + 64) : i for i in range(1, 27)}
    answer = []
    while msg:
        for i in range(len(msg), -1, -1):
            if msg[0:i] in dic:
                answer.append(dic[msg[0:i]])
                dic[msg[0:i+1]] = len(dic) + 1
                msg = msg[i:]
                break
    return answer