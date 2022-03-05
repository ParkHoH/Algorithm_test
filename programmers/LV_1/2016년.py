import datetime

def solution(a, b):
    weekday = ["MON","TUE","WED","THU","FRI","SAT", "SUN"]
    return weekday[datetime.date(2016, a, b).weekday()]

print(solution(5, 24))