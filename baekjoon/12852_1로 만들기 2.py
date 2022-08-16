from collections import deque

N = int(input())
visited = [False] * (N+1)
visited[N] = True
new_L = [0, [N]]
queue = deque()
queue.append(new_L)

while queue:
    cnt, L = queue.popleft()
    
    if L[-1]%3 == 0 and not visited[L[-1]//3]:
        visited[L[-1]//3] = True
        new_L = [cnt+1, L+[L[-1]//3]]
        if L[-1]//3 == 1:
            break
        queue.append(new_L)
        
    if L[-1]%2 == 0 and not visited[L[-1]//2]:
        visited[L[-1]//2] = True
        new_L = [cnt+1, L+[L[-1]//2]]
        if L[-1]//2 == 1:
            break
        queue.append(new_L)
        
    if L[-1]-1 >= 1 and not visited[L[-1]-1]:
        visited[L[-1]-1] = True
        new_L = [cnt+1, L+[L[-1]-1]]
        if L[-1]-1 == 1:
            break
        queue.append(new_L)

print(new_L[0])
for i in new_L[1]:
    print(i, end=" ")