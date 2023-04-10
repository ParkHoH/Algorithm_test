from collections import defaultdict

def solution(players, callings):
    dic_player = defaultdict(int)
    dic_idx = defaultdict(str)

    for i, player in enumerate(players):
        dic_player[player] = i
        dic_idx[i] = player

    for calling in callings:
        cur_idx = dic_player[calling]
        pre_player = dic_idx[cur_idx-1]
        
        dic_idx[cur_idx], dic_idx[cur_idx-1] = dic_idx[cur_idx-1], dic_idx[cur_idx]
        dic_player[calling] = cur_idx-1
        dic_player[pre_player] = cur_idx

    answer = []

    for player in dic_idx.values():
        answer.append(player)

    return answer


print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))
