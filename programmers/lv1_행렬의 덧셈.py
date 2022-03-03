#my solution
def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[i])):
            temp.append(arr1[i][j] + arr2[i][j])
        answer.append(temp)

    return answer

#best solution
def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] += arr2[i][j]
    
    return arr1

#other solution
def solution(arr1, arr2):
    answer = [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]

    return answer