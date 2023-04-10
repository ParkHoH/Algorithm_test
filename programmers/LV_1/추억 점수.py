from collections import defaultdict

def solution(name, yearning, photo):
    dic = defaultdict(int)

    for i in range(len(name)):
        dic[name[i]] = yearning[i]

    answer = []

    for p in photo:
        score = 0

        for n in p:
            score += dic[n]

        answer.append(score)

    return answer


print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))