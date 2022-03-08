import re
def solution(s):
    string = s.split(' ')
    for i in range(len(string)):
        if string[i] != '':
            string[i] = re.sub('^[a-z]', string[i][0].upper(), string[i])
            string[i] = string[i][0] + string[i][1:].lower()
    
    return ' '.join(string)


#better solution
def solution(s):
    string = s.split(' ')
    for i in range(len(string)):
        if string[i] != '':
            string[i] = string[i][0].upper() + string[i][1:].lower()
    return ' '.join(string)