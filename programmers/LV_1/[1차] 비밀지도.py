def solution(n, arr1, arr2):
    result = []

    arr1 = list(map(bin, arr1))
    arr2 = list(map(bin, arr2))
    
    max_len = 0    
    for i in range(n):
        arr1[i] = arr1[i][2:]
        arr2[i] = arr2[i][2:]
        max_len = max(max_len, len(arr1[i]), len(arr2[i]))
        
    for i in range(n):
        if max_len - len(arr1[i]) != 0:
            arr1[i] = '0' * (max_len - len(arr1[i])) + arr1[i] 
        if max_len - len(arr2[i]) != 0:
            arr2[i] = '0' * (max_len - len(arr2[i])) + arr2[i] 
    
    for i in range(n):
        temp_list = ''
        for j in range(len(arr1[i])):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                temp_list += '#'
            else:
                temp_list += ' '
        result.append(temp_list)
        
    return result


#better code
def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        result = bin(i|j)[2:]
        result = result.rjust(n, '0')
        result = result.replace('1', '#')
        result = result.replace('0', ' ')
        answer.append(result)
    return result