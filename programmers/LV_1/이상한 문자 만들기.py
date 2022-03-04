def solution(s):
    L = list(s.split(' '))
    new_list = []

    for i in L:
        new_string = ''
        for j in range(len(i)):
            if j % 2 == 0:
                new_string += i[j].upper()
            else:
                new_string += i[j].lower()
        new_list.append(new_string)

    return ' '.join(new_list)


#better code
def solution(s):
    new_list = []

    for i in list(s.split(' ')):
        new_string = ''
        for j in range(len(i)):
            new_string += i[j].upper() if j % 2 == 0 else i[j].lower()
        new_list.append(new_string)

    return ' '.join(new_list)