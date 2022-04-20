def solution(n, k, cmd):
    linked = {i: [i-1, i+1] for i in range(n)}
    linked[0], linked[n-1] = [None, 1], [n-2, None]
    eliminated_list = []
    result = ["O"] * n
    for command in cmd:
        if command[0] == "D" or command[0] == "U": # 커서 이동
            direction, num = command.split()
            if direction == "D":
                for _ in range(int(num)):
                    k = linked[k][1]
            else:
                for _ in range(int(num)):
                    k = linked[k][0]
            
        elif command == "C": # 삭제
            result[k] = "X"
            prev, after = linked[k]
            eliminated_list.append([k, prev, after])
            k = prev if after == None else after
            if prev == None:
                linked[after][0] = prev
            elif after == None:
                linked[prev][1] = after
            else:
                linked[prev][1] = after
                linked[after][0] = prev
        
        else: # 되돌리기
            idx, prev, after = eliminated_list.pop()
            result[idx] = "O"
            if prev and after:
                linked[prev][1] = idx
                linked[after][0] = idx
            elif prev:
                linked[prev][1] = idx
            elif after:
                linked[after][0] = idx
                
    return ''.join(result)


# my solution: 잘못된 부분
def solution(n, k, cmd):
    cmd = [command.split() for command in cmd]
    L = []
    L.append([0, 0, 1, "O"])
    for i in range(1, n-1):
        L.append([i, i-1, i+1, "O"])
    L.append([n-1, n-2, n-1, "O"])
    delete = []
        
    for command in cmd:
        if command[0] == "D":
            cnt = 0
            while cnt != int(command[1]):
                if k == L[k][2]:
                    break
                k = L[k][2]
                cnt += 1
                
        elif command[0] == "U":
            cnt = 0
            while cnt != int(command[1]):
                if k == L[k][1]:
                    break
                k = L[k][1]
                cnt += 1
                    
        elif command[0] == "C":
            L[k][3] = "X"
            delete.append(k)
            if k == L[k][2]:
                L[L[k][1]][2] = L[k][1]
            elif k == L[k][1]:
                L[L[k][2]][1] = L[k][2]
            else:
                L[L[k][1]][2] = L[k][2]
                L[L[k][2]][1] = L[k][1]

            if L[k][2] == k:
                k = L[k][1]
            else:
                k = L[k][2]
        
        elif command[0] == "Z":
            idx = delete.pop()
            L[idx][3] = "O"
            for i in range(idx-1, -1, -1):
                if L[i][3] == "O":
                    L[idx][1] = i
                    if L[i][2] == i:
                        L[idx][2] = idx
                    else:
                        L[L[i][2]][1] = idx
                        L[idx][2] = L[i][2]
                    L[i][2] = idx
            else:
                L[idx][1] = L[idx][2] = idx
            
    return ''.join([result[3] for result in L])


# 시간 초과 
def solution(n, k, cmd):
    cmd = [command.split() for command in cmd]
    L = []
    for i in range(n):
        L.append([i, "O"])
    delete = []
        
    for command in cmd:
        if command[0] == "D":
            cnt = 0
            while cnt != int(command[1]):
                if k == n-1:
                    break
                k += 1
                if L[k][1] == "O":
                    cnt += 1
                
        elif command[0] == "U":
            cnt = 0
            while cnt != int(command[1]):
                if k == 0:
                    break
                k -= 1
                if L[k][1] == "O":
                    cnt += 1
                    
        elif command[0] == "C":
            L[k][1] = "X"
            ori_k = k
            delete.append(k)
            cnt = 0
            while cnt != 1:
                if k == n-1:
                    k = ori_k
                    while cnt != 1:
                        if k == 0:
                            break
                        k -= 1
                        if L[k][1] == "O":
                            cnt += 1
                    break
                k += 1
                if L[k][1] == "O":
                    cnt += 1
        
        elif command[0] == "Z":
            idx = delete.pop()
            L[idx][1] = "O"
            
    return ''.join([result[1] for result in L])

print(solution(	8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))