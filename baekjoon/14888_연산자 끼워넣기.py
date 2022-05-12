from itertools import permutations

N = int(input())
L = list(map(int, input().split()))
plus, minus, mutiply, divide = map(int, input().split())
operator = ['+'] * plus + ['-'] * minus + ['*'] * mutiply + ['/'] * divide
set_operator = set()
max_value, min_value = -float('inf'), float('inf')

for permu in permutations(operator, N-1):
    if permu in set_operator:
        continue
    set_operator.add(permu)

    num = L[0]
    for i in range(N-1):
        if permu[i] == '+':
            num += L[i+1]
        elif permu[i] == '-':
            num -= L[i+1]
        elif permu[i] == '*':
            num *= L[i+1]
        elif permu[i] == '/':
            num = int(num / L[i+1])
    
    max_value = max(max_value, num)
    min_value = min(min_value, num)

print(max_value)
print(min_value)