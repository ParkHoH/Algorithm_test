def solution(s):
    if len(s) == 4 or len(s) == 6:
        try:
            s = int(s)
            return True
        except:
            return False
    else:
        return False

#modified code
def solution(s):
    try:
        s = int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6 #단, len 함수의 경우 O(1)의 시간이 걸리니 앞에 있는 것이 효율성이 높음

#better code
def solution(s):
    return s.isdigit() and len(s) in (4, 6)