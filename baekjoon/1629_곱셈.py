A, B, C = map(int, input().split())
A %= C
B %= C

def find(a, b):
    if b == 1:
        return a % C
    
    else:
        num = find(a, b//2)
        if b % 2 == 0:
            return ((num % C) * (num % C)) % C
        else:
            return (A * (num % C) * (num % C)) % C

print(find(A, B))