from collections import defaultdict

def solution(commands):
    merged = [[-1] * 50 for _ in range(50)]
    merge_group_idx = 0

    merge_dict = defaultdict(list) # merge 그룹에 따른 구성원들
    str_dict = defaultdict(set) # 문자열에 따른 좌표값
    xy_dict = defaultdict(str) # 좌표값에 따른 문자열

    parent = {}

    for x in range(50):
        for y in range(50):
            parent[(x, y)] = (x, y)

    result = []

    def find(xy):
        if xy != parent[xy]:
            parent[xy] = find(parent[xy])

        return parent[xy]

    for command in commands:
        c = command.split()

        if c[0] == "UPDATE":
            if len(c) == 4: # UPDATE r c value
                x, y = find((int(c[1])-1, int(c[2])-1))
                new_str = c[3]

                if (x, y) in xy_dict and len(xy_dict[(x, y)]): # 기존에 문자가 있던 경우
                    ori_str = xy_dict[(x, y)]
                    str_dict[ori_str].remove((x, y))
                    
                str_dict[new_str].add((x, y))
                xy_dict[(x, y)] = new_str

            else: # UPDATE value1 value2
                value1, value2 = c[1], c[2]

                for x, y in str_dict[value1]:
                    x, y = find((x, y))
                    xy_dict[(x, y)] = value2
                    str_dict[value2].add((x, y))

                str_dict[value1] = set()


        elif c[0] == "MERGE":
            _, x1, y1, x2, y2 = c
            x1, y1, x2, y2 = int(x1)-1, int(y1)-1, int(x2)-1, int(y2)-1 

            x1, y1 = find((x1, y1)) # 부모 찾기
            x2, y2 = find((x2, y2))
            parent[(x2, y2)] = (x1, y1)

            value = ""

            if (x1, y1) in xy_dict and len(xy_dict[(x1, y1)]):
                value = xy_dict[(x1, y1)]

            if (x2, y2) in xy_dict and len(xy_dict[(x2, y2)]):
                tmp_value = xy_dict[(x2, y2)]
                if value == "":
                    value = tmp_value

                str_dict[tmp_value].remove((x2, y2))
                xy_dict[(x2, y2)] = ""

            str_dict[value].add((x1, y1))
            xy_dict[(x1, y1)] = value

            if merged[x1][y1] != -1: # 기존에 merge 되어 있는 경우
                group_idx = merged[x1][y1]

                if merged[x2][y2] != -1: # x2, y2가 기존에 merge 되어 있는 경우
                    added_group_idx = merged[x2][y2]

                    for x, y in merge_dict[added_group_idx]:
                        merged[x][y] = group_idx

                    merge_dict[group_idx] += merge_dict[added_group_idx]
                    merge_dict[added_group_idx] = []
                
                else: # x2, y2가 처음 merge 하는 경우
                    merged[x2][y2] = group_idx
                    merge_dict[group_idx].append((x2, y2))

            else: # 처음 merge 하는 경우
                if merged[x2][y2] != -1: # x2, y2가 기존에 merge 되어 있는 경우
                    added_group_idx = merged[x2][y2]
                    merged[x1][y1] = added_group_idx
                    merge_dict[added_group_idx].append((x1, y1))
                
                else: # x2, y2가 처음 merge 하는 경우
                    merge_dict[merge_group_idx].append((x1, y1))
                    merge_dict[merge_group_idx].append((x2, y2))
                    merged[x1][y1] = merge_group_idx
                    merged[x2][y2] = merge_group_idx

                    merge_group_idx += 1


        elif c[0] == "UNMERGE":
            _, x, y = c
            x, y = int(x)-1, int(y)-1
            group_idx = merged[x][y]

            if group_idx != -1:
                parent_x, parent_y = find((x, y))
                value = xy_dict[(parent_x, parent_y)]

                xy_dict[(parent_x, parent_y)] = ""
                if (parent_x, parent_y) in str_dict[value]:
                    str_dict[value].remove((parent_x, parent_y))

                xy_dict[(x, y)] = value
                str_dict[value].add((x, y))

                for x1, y1 in merge_dict[group_idx]:
                    parent[(x1, y1)] = (x1, y1)
                    merged[x1][y1] = -1

                merged[x][y] = -1
                merge_dict[group_idx] = []
        

        elif c[0] == "PRINT":
            x, y = find((int(c[1])-1, int(c[2])-1))
            if (x, y) in xy_dict and len(xy_dict[(x, y)]):
                result.append(xy_dict[(x, y)])
            else:
                result.append("EMPTY")

    return result

print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))
print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))