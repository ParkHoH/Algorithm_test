def solution(genres, plays):
    # 자료구조: dictionary
    # key: genres / value: [총합, [[plays, index], [plays, index], ... ]]
    dic = {}
    
    # genres와 plays를 쌍으로 dictionary에 넣어주기
        # genre가 없을 경우 초기 세팅
        # 있을 경우 총합은 더해주고, 배열에는 append 해줌
    i = 0
    for genre, play in zip(genres, plays):
        if genre in dic:
            dic[genre][0] += play
            dic[genre][1].append([play, i])
        else:
            dic[genre] = [play, [[play, i]]]
        i += 1
        
    # dictinary 자체를 총합에 따라 정렬해줌
    # dictinary 각 원소마다 배열의 값을 정렬해줌
    d = sorted(dic.items(), key=lambda x: x[1][0], reverse=True)
    result = []
    target_length = len(genres) if len(genres)%2 == 0 else len(genres)-1
    for i in range(len(d)):
        d[i][1][1].sort(reverse=True)
        for _, idx in d[i][1][1]:
            result.append(idx)
            if len(result) == target_length:
                break

    return result
    
    
    # 장르수//2 만큼 dictionary의 values를 하나씩 결과값에 넣어줌
    
    
print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]	))