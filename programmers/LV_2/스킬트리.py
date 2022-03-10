def solution(skill, skill_trees):
    cnt = 0
    skill = skill[::-1]
    for skill_tree in skill_trees:
        s = skill
        flag = False
        while s:
            if s[0] in skill_tree:
                idx = skill_tree.index(s[0])
                skill_tree = skill_tree[:idx]
                flag = True
            elif flag:
                break
            s = s[1:]
        cnt = cnt if flag and s else cnt + 1
    return cnt


#better solution
def solution(skill, skill_trees):
    cnt = 0
    for skill_tree in skill_trees:
        skill_list = ''
        for i in skill_tree:
            if i in skill:
                skill_list += i
        if skill_list == skill[:len(skill_list)]:
            cnt += 1
    return cnt


print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))