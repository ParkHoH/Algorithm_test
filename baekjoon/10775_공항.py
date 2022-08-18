import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
gate = [False] * (G+1)
plane = [0] * P

for i in range(P):
    plane[i] = int(input())

result = 0
possible = True

for g in plane:
    while True:
        if g < 1:
            possible = False
            break
        
        if not gate[g]: 
            result += 1
            gate[g] = True
            break

        g -= 1
    
    if not possible:
        break

print(result)