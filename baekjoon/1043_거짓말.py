from collections import deque

N, M = map(int, input().split())
t_people, *truth = list(map(int, input().split()))
parties = []
graph = [set() for _ in range(N+1)]

for _ in range(M): # 연결짓기
    people = list(map(int, input().split()))
    parties.append(people)

    for i in range(1, len(people)):
        for j in range(i+1, len(people)):
            graph[people[i]].add(people[j])
            graph[people[j]].add(people[i])

polluted = [False] * (N+1)
queue = deque()

for person in truth:
    queue.append(person)
    polluted[person] = True

while queue:
    person = queue.popleft()

    for p in graph[person]:
        if not polluted[p]:
            queue.append(p)
            polluted[p] = True

result = 0

for party in parties:
    possible = True

    for i in range(1, party[0]+1):
        if polluted[party[i]]:
            possible = False
            break
    
    if possible:
        result += 1

print(result)