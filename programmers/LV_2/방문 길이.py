def solution(dirs):
    L = []
    x, y = 0, 0
    
    UDRL = {"U": 1, "D": -1, "R": 1, "L": -1}
    
    for s in dirs:
        if (s == "R" and x < 5) or (s == "L" and x > -5):
            if [x, y, x+UDRL[s], y] not in L:
                L.append([x, y, x+UDRL[s], y])
                L.append([x+UDRL[s], y, x, y])
            x += UDRL[s]
        elif (s == "U" and y < 5) or (s == "D" and y > -5):
            if [x, y, x, y+UDRL[s]] not in L:
                L.append([x, y, x, y+UDRL[s]])
                L.append([x, y+UDRL[s], x, y])
            y += UDRL[s]

    return len(L) // 2


#better solution
def solution(dirs):
    set_dirs = set()
    xy = [0, 0]
    
    UDRL = {"U": [0, 1], "D": [0, -1], "R": [1, 0], "L": [-1, 0]}
    
    for s in dirs:
        x, y = xy[0] + UDRL[s][0], xy[1] + UDRL[s][1]
        if -5 <= x <= 5 and -5 <= y <= 5:
            set_dirs.add((xy[0], xy[1], x, y))
            set_dirs.add((x, y, xy[0], xy[1]))
            xy = [x, y]
    return len(set_dirs) // 2