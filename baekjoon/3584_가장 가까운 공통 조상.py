from collections import defaultdict
import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    N = int(input())
    graph = defaultdict(int)

    for _ in range(N-1):
        parent, child = map(int, input().split())
        graph[child] = parent

    node1, node2 = map(int, input().split())
    target = set()
    target.add(node1)

    global answer
    answer = -1

    def find_parent1(node):
        parent = graph[node]
        if parent == 0: return

        target.add(parent)
        find_parent1(parent)
    
    def find_parent2(node):
        if node in target:
            global answer
            answer = node
            return

        parent = graph[node]
        if parent == 0: return

        find_parent2(parent)

    find_parent1(node1)
    find_parent2(node2)

    print(answer)