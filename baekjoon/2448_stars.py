import sys
sys.setrecursionlimit(10**6)

def recursion_stars(n):
    if n == 1:
        return '*'
    
    stars = recursion_stars(n//2)
    list_stars = []
    num = (n//3) * 5
    
    for star in stars:
        list_stars.append(' '*int(2/5 * num) + star + ' '*int(2/5 * num))
    for star in stars:
        list_stars.append(' '*int(1/5 * num) + star + ' '*int(1/5 * num) + star + ' '*int(1/5 * num))
    for star in stars:
        list_stars.append(star*5)
    
    return list_stars

n = int(input())
print('\n'.join(recursion_stars(n)))