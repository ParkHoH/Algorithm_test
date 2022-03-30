def solution(name):
    answer = 0
    min_move = len(name) - 1
    for i, alphabet in enumerate(name):
        answer += min(ord(alphabet) - ord('A'), ord('Z') - ord(alphabet) + 1)
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) -next)]) 
        
    answer += min_move
    return answer

print(solution("JEROEN"))
print(solution("JAN"))


# def solution(name):
#     result = []
#     for alphabet in name:
#         result.append(min(ord(alphabet)-ord("A"), 91-ord(alphabet)))
#     idx = 0
#     answer = 0
#     while True:
#         answer += result[idx]
#         result[idx] = 0
#         if sum(result) == 0:
#             return answer
#         left = right = 1
#         while result[idx-left] == 0: # out of index 안 나는지?
#             left += 1
#             if abs(idx-left) == len(result)-1: 
#                 left = 100
#                 break
#         while result[idx+right] == 0:
#             right += 1
#             if abs(idx+right) == len(result)-1:
#                 right = 100
#                 break
#         answer += left if left < right else right
#         idx += -left if left < right else right