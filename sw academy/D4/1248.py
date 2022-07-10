from collections import defaultdict

def find_parent(node, graph):
    L = []
    stack = [node]
    while stack:
        node = stack.pop()
        if node in graph:
            stack.append(graph[node])
            L.append(graph[node])
    
    return L

TC = int(input())
for t in range(1, TC+1):
    V, E, node_1, node_2 = map(int, input().split())
    L = list(map(int, input().split()))
    graph_child = defaultdict(list)
    graph_parent = {}
    for i in range(E-1, -1, -1):
        graph_child[L[2*i]].append(L[2*i + 1])
        graph_parent[L[2*i + 1]] = L[2*i]
    
    L_node_1 = find_parent(node_1, graph_parent)
    L_node_2 = find_parent(node_2, graph_parent)
    result = [0, 0]
    stop = False
    for i in L_node_1:
        for j in L_node_2:
            if j == i:
                stop = True
                result[0] = j
                break
        if stop: break

    stack = [result[0]]
    while stack:
        node = stack.pop()
        result[1] += 1
        for i in graph_child[node]:
            stack.append(i)

    print(f'#{t} {result[0]} {result[1]}')


# from collections import defaultdict

# TC = int(input())
# for t in range(1, TC+1):
#     V, E, node_1, node_2 = map(int, input().split())
#     graph_child = defaultdict(list)
#     L = list(map(int, input().split()))
#     L_node_1 = [node_1]
#     L_node_2 = [node_2]
#     for i in range(E-1, -1, -1):
#         graph_child[L[2*i]].append(L[2*i + 1])
#         if L[2*i + 1] in L_node_1:
#             L_node_1.append(L[2*i])

#         if L[2*i + 1] in L_node_2:
#             L_node_2.append(L[2*i])

#     result = [0, 0]
#     stop = False
#     for i in L_node_1:
#         for j in L_node_2:
#             if j == i:
#                 stop = True
#                 result[0] = j
#                 break
#         if stop: break

#     stack = [result[0]]
#     while stack:
#         node = stack.pop()
#         result[1] += 1
#         for i in graph_child[node]:
#             stack.append(i)

#     print(f'#{t} {result[0]} {result[1]}')