def check_right(p):
    L = []
    for bracket in p:
        if len(L) == 0:
            L.append(bracket)
        else:
            L.pop() if bracket == ")" and L[-1] == "(" else L.append(bracket)
    return True if len(L) == 0 else False

def split_U_V(p):
    U = []
    cnt_left = cnt_right = 0
    for bracket in p:
        if bracket == "(":
            cnt_left += 1
        else:
            cnt_right += 1
        U.append(bracket)
        if cnt_left == cnt_right:
            V = p[cnt_left+cnt_right:]
            break
    return [''.join(U), V]

def solution(p):
    if not p:
        return ""
    U, V = split_U_V(p)
    if check_right(U):
        return U + solution(V)
    else:
        s = "(" + solution(V) + ")"
        U = list(U[1:-1])
        for i in range(len(U)):
            U[i] = ")" if U[i] == "(" else "("
        s += ''.join(U)
        return s

print(solution("()))((()"))