import sys
input = sys.stdin.readline

while True:
    m, n = map(int, input().split())

    if m == n == 0:
        break

    graph = []

    for _ in range(n):
        a, b, c = map(int, input().split())
        graph.append([a, b, c])

    def union_find(x):
        if x != parent[x]:
            parent[x] = union_find(parent[x])
        return parent[x]

    parent = [i for i in range(m)]

    graph.sort(key=lambda x: x[2])
    connected = set()
    connected.update((graph[0][0], graph[0][1]))
    result = 0

    for x, y, z in graph:
        i = union_find(x)
        j = union_find(y)

        if i > j:
            parent[i] = j
            result += z
        elif i < j:
            parent[j] = i
            result += z

    print(result)



# 시간 초과 : 링크드 리스트가 잘못된 것 같음
# import sys
# input = sys.stdin.readline

# while True:
#     m, n = map(int, input().split())

#     if m == n == 0:
#         break

#     graph = []
#     sum = 0

#     for _ in range(n):
#         a, b, c = map(int, input().split())
#         graph.append([a, b, c])
#         sum += c

#     graph.sort(key=lambda x: x[2])
#     for i in range(n):
#         graph[i] += [i-1, i+1]
    
#     graph[1][3] = 1
#     graph[n-1][4] = n-1
#     start = 1
#     end = n-1

#     connected = set()
#     connected.update((graph[0][0], graph[0][1]))
#     result = graph[0][2]
    
#     while len(connected) != m:
#         idx = start
#         for _ in range(len(connected)):
#             x, y, z, pre_node, post_node = graph[idx]

#             if x in connected and y in connected:
#                 idx = post_node
#                 continue

#             if x in connected or y in connected:
#                 if idx == start:
#                     start = post_node
#                     graph[post_node][3] = post_node

#                 elif idx == end:
#                     end = pre_node
#                     graph[pre_node][4] = pre_node
                
#                 else:
#                     graph[pre_node][4] = post_node
#                     graph[post_node][3] = pre_node

#                 connected.update([x, y])
#                 result += z
#                 break

#             idx = post_node # 다음 노드로 갱신

#     print(sum - result)



# 시간 초과: O(mn) -> m이 최대 200000 / n이 최대 200000
# import sys
# input = sys.stdin.readline

# while True:
#     m, n = map(int, input().split())

#     if m == n == 0:
#         break

#     graph = []
#     sum = 0

#     for _ in range(n):
#         a, b, c = map(int, input().split())
#         graph.append([a, b, c])
#         sum += c

#     graph.sort(key=lambda x: x[2])
#     connected = set()
#     connected.update((graph[0][0], graph[0][1]))
#     result = graph[0][2]
    
#     while len(connected) != m:
#         for x, y, z in graph:
#             if x in connected and y in connected:
#                 continue

#             if x in connected or y in connected:
#                 connected.update([x, y])
#                 result += z
#                 break

#     print(sum - result)


