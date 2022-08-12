from collections import defaultdict

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
checked = [False] * 101

def dfs(person):
    global cnt
    if cnt == N:
        return

    return

for person in people:
    global cnt
    cnt = 1
    dfs(person)
