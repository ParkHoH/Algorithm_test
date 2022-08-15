from collections import defaultdict

def solution(M, load):
    dic = defaultdict(int)
    load.sort(reverse=True)

    if load[0] > M:
        return -1

    for i in load:
        dic[i] += 1

    result = 0

print(solution(25, [5, 25, 13, 16, 15, 9, 17, 1, 3])) # 5
print(solution(30, [11, 5, 14, 29, 3, 1, 20, 19, 26, 8, 11, 14, 16]))