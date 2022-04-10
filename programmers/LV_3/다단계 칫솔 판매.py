import sys
sys.setrecursionlimit(10**6)

def solution(enroll, referral, seller, amount):
    dic = {person: [[], '', [], False] for person in enroll}
    for person, recommender in zip(enroll, referral):
        if recommender != "-":
            dic[recommender][0].append(person)
            dic[person][1] = recommender
    for person, money in zip(seller, amount):
        dic[person][2].append(money*100)
    
    def dfs(person):
        for connected_person in dic[person][0]:
            if dic[connected_person][3] == False:
                dfs(connected_person)

        dic[person][3] = True
        for i in range(len(dic[person][2])):
            money_distributed = int(dic[person][2][i] * 0.1)
            if money_distributed == 0:
                continue
            money_earned = dic[person][2][i] - money_distributed
            dic[person][2][i] = money_earned
            if dic[person][1]:
                dic[dic[person][1]][2].append(money_distributed)
    
    for person in dic.keys():
        if dic[person][3] == False:
            dfs(person)
    
    return [sum(value[2]) for value in dic.values()]



# Original Solution: 시간 초과로 dfs를 고려해서 풀었으나,
# 분배금이 0인 경우 break 하도록 구현하니 정상 작동
def solution(enroll, referral, seller, amount):
    dic = {person: [recommender, 0] for person, recommender in zip(enroll, referral)}
    amount = [money*100 for money in amount]
    
    for person, money in zip(seller, amount):
        while True:
            money_distributed = int(money * 0.1)
            money_earned = money - money_distributed
            dic[person][1] += money_earned
            if money_distributed == 0 or dic[person][0] == "-":
                break
            person, money = dic[person][0], money_distributed
    
    return [money for _, money in dic.values()]



print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))