from collections import defaultdict, deque

N, M = map(int, input().split())
relation = defaultdict(list)
people = set()

for _ in range(M):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)
    people.add(a)
    people.add(b)

for k, v in relation.items():
    relation[k] = list(set(v))

people = list(set(people))
people.sort()
result = [0, float('inf')]

for person in people:
    cnt = 1
    sum = 0
    queue = deque()
    queue.append([person, 1])
    checked = [False] * 101
    checked[person] = True

    while queue:
        p, depth = queue.popleft()
        for cp in relation[p]:
            if cnt == N:
                break

            if not checked[cp]:
                checked[cp] = True
                cnt += 1
                sum += depth
                queue.append([cp, depth+1])

    if sum < result[1]:
        result = [person, sum]

print(result[0])