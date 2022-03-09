import math

def timeToMinutes(time):
    hour, minute = map(int, time.split(":"))
    return hour*60 + minute

def solution(fees, records):
    dic = {}
    for record in records:
        L = record.split()
        key = L[1]
        time = L[0]
        if key not in dic:
            dic[key] = [time, 0, 0] #[입차 시간, 누적 시간, 요금]
        
        else:
            if dic[key][0] == 0:
                dic[key][0] = time
            else:
                time_L = timeToMinutes(time)
                time_dic = timeToMinutes(dic[key][0])
                dic[key][1] += time_L - time_dic
                dic[key][0] = 0

    for key, value in dic.items():
        if value[0] != 0:
            time_L = timeToMinutes("23:59")
            time_dic = timeToMinutes(dic[key][0])
            dic[key][1] += time_L - time_dic
            dic[key][0] = 0
        if dic[key][1] <= fees[0]:
            fee = fees[1]
        else:
            fee = fees[1] + math.ceil((dic[key][1] - fees[0])/fees[2]) * fees[3]
        dic[key][2] = fee
    
    return [item[1][2] for item in sorted(dic.items())]