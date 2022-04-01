# my solution
def solution(phone_book):
    dic = {}
    for num in phone_book:
        if len(num) in dic:
            dic[len(num)].append(num)
        else:
            dic[len(num)] = [num]
    for key, value in dic.items():
        dic[key] = sorted(value)
    
    for i in range(1, 20):
        if i in dic:
            for j in range(i+1, 21):
                if j in dic:
                    start = 0
                    for k in range(len(dic[i])):
                        for l in range(start, len(dic[j])):
                            if dic[i][k] < dic[j][l][:i]:
                                start = l
                                break
                            elif dic[i][k] == dic[j][l][:i]:
                                return False
    return True

# better solution
def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True