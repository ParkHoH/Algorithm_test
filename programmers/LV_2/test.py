from itertools import product

result = list(map(''.join, product(('a', 'b', 'c'))))
print(result)