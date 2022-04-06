def solution(record):
    record = [rc.split() for rc in record]
    dic_id = {}
    for rc in record:
        if rc[0] == "Enter" or rc[0] == "Change":
            dic_id[rc[1]] = rc[2]
    
    result = []
    for rc in record:
        if rc[0] == "Enter":
            result.append(dic_id[rc[1]] + "님이 들어왔습니다.")
        elif rc[0] == "Leave":
            result.append(dic_id[rc[1]] + "님이 나갔습니다.")
    return result
    

# more simple code
def solution(record):
    record = [rc.split() for rc in record]
    dic_id = {}
    for rc in record:
        if rc[0] == "Enter" or rc[0] == "Change":
            dic_id[rc[1]] = rc[2]
    
    result = []
    dic_printer = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    for rc in record:
        if rc[0] in dic_printer:
            result.append(dic_id[rc[1]] + dic_printer[rc[0]])
    return result