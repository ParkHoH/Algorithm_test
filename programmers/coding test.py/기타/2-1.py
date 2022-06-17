def solution(goods):
    dic = {}
    result = [[] for i in range(len(goods))]
    for i in range(len(goods)): # goods 선택
        for length in range(1, len(goods[i])+1): # 길이 1씩 증가 시키기
            for j in range(len(goods[i])): # 시작 위치 지정
                flag = True
                if j+length > len(goods[i]):
                    break

                word = goods[i][j:j+length]
                if word in dic: # 해당 단어가 dictionary에 있으면 continue
                    continue

                for k in range(i+1, len(goods)): # 다른 goods에 있는지 확인(많을 때)
                    if word in goods[k]:
                        dic[word] = 0
                        flag = False
                        break
                if flag:
                    for k in range(i): # 다른 goods에 있는지 확인(적을 때)
                        if word in goods[k]:
                            dic[word] = 0
                            flag = False
                            break

                if flag:
                    dic[word] = 0
                    result[i].append(word)

            if len(result[i]) > 0: # 단어 1개라도 추가된 경우 break
                result[i].sort()
                result[i] = ' '.join(result[i])
                break
            elif length == len(goods[i]):
                result[i] = "None"
    return result


print(solution(["abcdeabcd","cdabe","abce","bcdeab"]))