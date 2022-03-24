def solution(citations):
    citations.sort(reverse=True)
    max_value = max(citations)
    for i in range(max_value, -1, -1):
        for j in range(len(citations)):
            if len(citations)-j-1 <= i <= j+1 and citations[j] >= i:
            # if len(citations)-i <= citations[j] <= i:
                return i

# def solution(citations):
#     citations.sort(reverse=True)
#     for n in range(1, len(citations)+1):
#         if len(citations)-n <= citations[n-1] <= n:
#             return citations[n-1]
#     return citations[-1]

print(solution([3, 0, 6, 1, 5]))
# print(solution([10, 9, 8, 4, 4, 1]))
# print(solution([3, 4, 5, 11, 15, 16, 17, 18, 19, 20]))