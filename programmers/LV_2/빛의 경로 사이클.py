# 문제에서 사이클이 만들어지는 원리를 정확히 이해 못함
def check_xy(x, y, length_x, length_y):
    if x >= length_x: 
        x = 0
    elif x < 0:
        x = length_x - 1
    elif y >= length_y: 
        y = 0
    elif y < 0:
        y = length_y - 1
    return (x, y)

def solution(grid):
    direct = ["minus_x", "plus_x", "minus_y", "plus_y"]
    result = []
    for i in range(4):
        x = y = 0
        direction = direct[i]
        cnt = 0
        set_xy = set()
        set_xy.add((0, 0, direction))
        while True:
            cnt += 1
            if direction == "plus_x":
                x += 1    
            elif direction == "minus_x":
                x -= 1
            elif direction == "plus_y":
                y += 1
            else:
                y -= 1
            x, y = check_xy(x, y, len(grid), len(grid[0]))

            if grid[x][y] == "L":
                if direction == "plus_x":
                    direction = "plus_y"
                elif direction == "minus_x":
                    direction = "minus_y"
                elif direction == "plus_y":
                    direction = "minus_x"
                elif direction == "minus_y":
                    direction = "plus_x"
                    
            elif grid[x][y] == "R":
                if direction == "plus_x":
                    direction = "minus_y"
                elif direction == "minus_x":
                    direction = "plus_y"
                elif direction == "plus_y":
                    direction = "plus_x"
                elif direction == "minus_y":
                    direction = "minus_x"
            
            if (x, y, direction) in set_xy:
                if x == y == 0:
                    result.append(cnt)
                break
            else:
                set_xy.add((x, y, direction))
    
    return result

print(solution(["R","R"]))