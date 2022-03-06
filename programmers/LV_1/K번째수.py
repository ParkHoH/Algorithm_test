def solution(array, commands):
    answer = []
    
    for command in commands:
        start = command[0] - 1
        end = command[1] - 1
        choice = command[2] - 1
        
        result = sorted(array[start:end+1])
        answer.append(result[choice])
    
    return answer


#better code
def solution(array, commands):
    answer = []
    
    for command in commands:
        start, end, choice = command
        result = sorted(array[start:end+1])
        answer.append(result[choice])
    
    return answer


#short code
def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))