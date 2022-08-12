# import sys
# input = sys.stdin.readline

# N = int(input())
# s = set()

# for _ in range(N):
#     oper = input().split()

#     if oper[0] == "add":
#         s.add(int(oper[1]))

#     elif oper[0] == "remove":
#         s.remove(int(oper[1]))

#     elif oper[0] == "check":
#         num = int(oper[1])
#         if num in s:
#             print(1)
#         else:
#             print(0)
    
#     elif oper[0] == "toggle":
#         num = int(oper[1])
#         if num in s:
#             s.remove(num)
#         else:
#             s.add(num)
    
#     elif oper[0] == "all":
#         s = set(range(1, 21))

#     elif oper[0] == "empty":
#         s = set()


s = set()
s.remove(1)