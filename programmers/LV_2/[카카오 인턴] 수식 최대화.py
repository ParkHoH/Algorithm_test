def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)



import re
from itertools import permutations

# eval 활용
def solution(expression):
    expression = re.findall('(\d+)(-|\+|\*)?', expression)
    operator = ['-', '*', '+']
    max_value = 0
    copy_expression = expression
    for permutation in permutations(operator, 3):
        expression = copy_expression
        for oper in permutation:
            start = 0
            while start != len(expression)-1:
                for i in range(start, len(expression)-1):
                    if oper == expression[i][1]:
                        temp = [eval(str(expression[i][0]) + oper + str(expression[i+1][0])), expression[i+1][1]]
                        expression = expression[:i] + [temp] + expression[i+2:]
                        break
                    start += 1  
                    
        max_value = max(max_value, abs(expression[0][0]))
    return max_value


# solution
import re
from itertools import permutations

def solution(expression):
    expression = re.findall('(\d+)(-|\+|\*)?', expression)
    operator = ['-', '*', '+']
    max_value = 0
    copy_expression = expression
    for permutation in permutations(operator, 3):
        expression = copy_expression
        for oper in permutation:
            start = 0
            while start != len(expression)-1:
                for i in range(start, len(expression)-1):
                    if oper == expression[i][1]:
                        if oper == '-':
                            temp = [int(expression[i][0]) - int(expression[i+1][0]), expression[i+1][1]]
                        elif oper == '+':
                            temp = [int(expression[i][0]) + int(expression[i+1][0]), expression[i+1][1]]
                        elif oper == '*':
                            temp = [int(expression[i][0]) * int(expression[i+1][0]), expression[i+1][1]]
                        expression = expression[:i] + [temp] + expression[i+2:]
                        break
                    start += 1
        max_value = max(max_value, abs(expression[0][0]))
    return max_value

print(solution("100-200*300-500+20"	))