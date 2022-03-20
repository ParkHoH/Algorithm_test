def solution(n, words):
    dic = {}
    for idx, word in enumerate(words):
        if word in dic:
            return [idx%n + 1, idx//n + 1]
        dic[word] = 1
    return [0, 0]