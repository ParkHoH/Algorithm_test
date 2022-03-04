def solution(n):
    L = []
    for i in str(int(n)):
        L.append(int(i))
    return L[::-1]

#better code
def solution(n):
    return list(map(int, reversed(str(n))))