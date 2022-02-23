import sys
sys.setrecursionlimit(10**6)

def recursion_stars(n):
    if n == 1:
        return '*'
        
    stars = recursion_stars(n//3)
    List_stars = []

    for star in stars:
        List_stars.append(star*3)
    for star in stars:
        List_stars.append(star + ' '*(n/3) + star)
    for star in stars:
        List_stars.append(star*3)
    return List_stars


n = int(input())
print('\n'.join(recursion_stars(n)))