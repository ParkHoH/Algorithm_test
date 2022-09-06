from collections import deque

def solution(rc, operations):
    rows = deque(deque(row[1:-1]) for row in rc)
    cols = [deque(rc[row][0] for row in range(len(rc))),
            deque(rc[row][-1] for row in range(len(rc)))]

    for operation in operations:
        if operation == "ShiftRow":
            rows.appendleft(rows.pop())
            cols[0].appendleft(cols[0].pop())
            cols[1].appendleft(cols[1].pop())
        
        else:
            rows[0].appendleft(cols[0].popleft())
            cols[1].appendleft(rows[0].pop())
            rows[-1].append(cols[1].pop())
            cols[0].append(rows[-1].popleft())
            
    return [[cols[0][r]] + list(rows[r]) + [cols[1][r]] for r in range(len(rc))]

print(solution([[1, 3], [4, 6]], ["ShiftRow"]))
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))