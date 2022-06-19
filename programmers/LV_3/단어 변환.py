from collections import deque

def solution(begin, target, words):
    dic = {}
    queue = deque()
    queue.append((begin, 0))
    while queue:
        word, cnt = queue.popleft()
        for i in range(len(begin)):
            for w in words:
                new_word = word[:i] + w[i] + word[i+1:]
                if new_word in dic:
                    continue
                
                if new_word in words:
                    if new_word == target:
                        return cnt+1

                    queue.append((new_word, cnt+1))
                    dic[new_word] = True
    
    return 0

print(solution("hit"	,"cog"	,	["hot", "dot", "dog", "lot", "log"]))