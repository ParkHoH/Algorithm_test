from itertools import permutations

def solution(graph):
    result = 0
    for permu in permutations(range(len(graph)), len(graph)):
        permu = list(permu)
        num = 0
        for i in range(len(graph)):
            num += graph[i][permu[i]]

        result = max(result, num)

    return result

print(solution([[22, 33], [33, 45]]))