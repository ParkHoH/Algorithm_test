def solution(today, terms, privacies):
    dic = {}
    for term in terms:
        a, b = term.split()
        dic[a] = int(b)
    
    def change_date(year, month, day, term):
        year = int(year)
        month = int(month)
        day = int(day)
        plus_month = dic[term]

        day -= 1

        if day == 0:
            plus_month -= 1
            day = 28

        month += plus_month

        if month % 12 == 0:
            plus_year = max(0, month//12 - 1)
            month = 12

        else:
            plus_year = month // 12
            month %= 12

        year += plus_year

        return [year, month, day]

    L = []

    for i, privacy in enumerate(privacies):
        dates, term = privacy.split()
        year, month, day = dates.split('.')
        L.append(change_date(year, month, day, term) + [i+1])

    L.sort(key=lambda x: (x[0], x[1], x[2]))
    
    std_year, std_month, std_day = today.split('.')
    std_year, std_month, std_day = int(std_year), int(std_month), int(std_day)

    result = []

    for year, month, day, i in L:
        if year > std_year:
            continue
        elif year == std_year:
            if month > std_month:
                continue
            elif month == std_month:
                if day >= std_day:
                    continue
                else:
                    result.append(i)
            else:
                result.append(i)
        else:
            result.append(i)

    result.sort()
    return result

print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))