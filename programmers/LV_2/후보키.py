from itertools import combinations

def solution(relation):
    L = []
    for num in range(1, len(relation[0])+1):
        combination = list(combinations(range(len(relation[0])), num))
        for comb in combination:
            temp = [tuple([relation[i][j] for j in comb]) for i in range(len(relation))]
            if len(set(temp)) == len(relation):
                notSubset = True
                for i in L:
                    if set(i).issubset(comb):
                        notSubset = False
                        break
                if notSubset:
                    L.append(comb)
    return len(L)

# from itertools import combinations

# def solution(relation):
#     result = 0
#     dic = {}
    
#     for num in range(1, len(relation[0])+1):
#         combination = list(combinations(range(len(relation[0])), num))
#         for comb in combination:
#             flag = False
#             for i in comb:
#                 if i in dic:
#                     flag = True
#                     break
#             if flag:
#                 continue
#             else:
#                 L = []
#                 for i in range(len(relation)):
#                     temp_L = []
#                     for j in comb:
#                         temp_L.append(relation[i][j])
#                     L.append(tuple(temp_L))
#                 if len(list(set(L))) == len(relation):
#                     result += 1
#                     if num == 1:
#                         dic[comb[0]] = 0
#     return result



    # for i in range(len(trans_relation)):
    #     if i in dic_exception:
    #         continue
    #     for j in range(i+1, len(trans_relation)):
    #         if j in dic_exception:
    #             continue
    #         set_combination = []
    #         for k in range(len(trans_relation[i])):
    #             set_combination.append((trans_relation[i][k], trans_relation[j][k]))
    #         set_combination = list(set(set_combination))
    #         if len(set_combination) == len(trans_relation[i]):
    #             result += 1

    # return result



print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))