from itertools import permutations

TC = int(input())
for t in range(1, TC+1):
    N = int(input())
    L = list(map(int, input().split()))
    company = L[:2]
    home = L[2:4]
    L = L[4:]
    location = {}
    for i in range(N):
        location[i] = [L[2*i], L[2*i + 1]]

    result = float('inf')
    for permu in permutations(range(N), N):
        num = 0
        x, y = company
        for i in permu:
            nx, ny = location[i]
            num += abs(x - nx) + abs(y - ny)
            x, y = location[i]
        
        num += abs(x - home[0]) + abs(y - home[1])
        result = min(result, num)

    print(f'#{t} {result}')