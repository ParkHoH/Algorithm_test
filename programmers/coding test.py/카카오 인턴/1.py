from collections import defaultdict

def solution(survey, choices):
    dic = defaultdict(int)
    for i in range(len(survey)):
        if choices[i] in range(1, 4):
            dic[survey[i][0]] += 4 - choices[i]
        elif choices[i] in range(5, 8):
            dic[survey[i][1]] += choices[i] - 4

    result = ""
    if dic["R"] >= dic["T"]:
        result += "R"
    else:
        result += "T"

    if dic["C"] >= dic["F"]:
        result += "C"
    else:
        result += "F"

    if dic["J"] >= dic["M"]:
        result += "J"
    else:
        result += "M"

    if dic["A"] >= dic["N"]:
        result += "A"
    else:
        result += "N"

    return result

print(solution(["AN", "CF", "MJ", "RT", "NA"],	[5, 3, 2, 7, 5]	))