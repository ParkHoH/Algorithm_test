def rotate(arr):
    temp = arr[0][0]
    for i in range(len(arr[0])-1):
        temp2 = arr[0][i+1]
        arr[0][i+1] = temp
        temp = temp2

    for i in range(len(arr)-1):
        temp2 = arr[i+1][len(arr[0])-1]
        arr[i+1][len(arr[0])-1] = temp
        temp = temp2

    for i in range(len(arr[0])-1, 0, -1):
        temp2 = arr[len(arr)-1][i-1]
        arr[len(arr)-1][i-1] = temp
        temp = temp2

    for i in range(len(arr)-1, 0, -1):
        temp2 = arr[i-1][0]
        arr[i-1][0] = temp
        temp = temp2

    return arr

def shift_row(arr):
    return [arr[-1]] + arr[:len(arr)-1]

def solution(rc, operations):
    new_operations = []
    cnt = 0
    for operation in operations:
        if not new_operations:
            new_operations.append(operation)
            continue
        if new_operations[-1] != operation:
            cnt = 0
        else:
            cnt += 1

        new_operations.append(operation)
        if cnt == len(rc) and new_operations[-1] == "ShiftRow":
            for _ in range(cnt):
                new_operations.pop()
            cnt = 0
        elif cnt == len(rc) * len(rc[0]) and new_operations[-1] == "Rotate":
            for _ in range(cnt):
                new_operations.pop()
            cnt = 0
        
    for operation in new_operations:
        if operation == "Rotate":
            rc = rotate(rc)
        else:
            rc = shift_row(rc)

    return rc

print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]))

# def rotate(arr):
#     temp = arr[0][0]
#     for i in range(len(arr[0])-1):
#         temp2 = arr[0][i+1]
#         arr[0][i+1] = temp
#         temp = temp2

#     for i in range(len(arr)-1):
#         temp2 = arr[i+1][len(arr[0])-1]
#         arr[i+1][len(arr[0])-1] = temp
#         temp = temp2

#     for i in range(len(arr[0])-1, 0, -1):
#         temp2 = arr[len(arr)-1][i-1]
#         arr[len(arr)-1][i-1] = temp
#         temp = temp2

#     for i in range(len(arr)-1, 0, -1):
#         temp2 = arr[i-1][0]
#         arr[i-1][0] = temp
#         temp = temp2

#     return arr

# def shift_row(arr):
#     return [arr[-1]] + arr[:len(arr)-1]

# def solution(rc, operations):
#     for operation in operations:
#         if operation == "Rotate":
#             rc = rotate(rc)
#         else:
#             rc = shift_row(rc)

#     return rc