L = list(map(int, input().split()))

result = ""
flag = True
for i in range(1, 9):
    if L[i-1] != i:
        flag = False
        break

if flag:
    result = "ascending"
else:
    idx = 0
    flag = True
    for i in range(8, 0, -1):
        if L[idx] != i:
            flag = False
            break
        idx += 1

    result = "descending" if flag else "mixed"
    
print(result)