def solution(answers):
    scores = [0, 0, 0]
    dic_1 = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
    dic_2 = {0: 2, 1: 1, 2: 2, 3: 3, 4: 2, 5: 4, 6: 2, 7: 5}
    dic_3 = {0: 3, 1: 3, 2: 1, 3: 1, 4: 2, 5: 2, 6: 4, 7: 4, 8: 5, 9: 5}
    
    for i in range(len(answers)):
        if dic_1[i%5] == answers[i]:
            scores[0] += 1
        if dic_2[i%8] == answers[i]:
            scores[1] += 1
        if dic_3[i%10] == answers[i]:
            scores[2] += 1
    
    max_score = max(scores)
    return [idx+1 for idx, score in enumerate(scores) if score == max_score]
            

#modified solution
def solution(answers):
    scores = [0, 0, 0]
    choice = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    for i in range(len(answers)):
        if choice[0][i%5] == answers[i]:
            scores[0] += 1
        if choice[1][i%8]  == answers[i]:
            scores[1] += 1
        if choice[2][i%10]  == answers[i]:
            scores[2] += 1
    
    max_score = max(scores)
    return [idx+1 for idx, score in enumerate(scores) if score == max_score]