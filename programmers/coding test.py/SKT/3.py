from bisect import bisect_left
from collections import defaultdict

def solution(n, plans, clients):
    # L: 이분 탐색을 위해 제공 데이터 순서대로 넣어준 리스트
    # dic_additional: 부가서비스가 포함된 요금제 번호 딕셔너리
    L = []
    dic_additional = defaultdict(int)
    for i in range(len(plans)):
        plan = plans[i].split()
        L.append(int(plan[0]))
        for num in plan[1:]:
            dic_additional[num] = i+1
    
    # 클라이언트 수만큼 반복하며 결과에 추가
    result = []
    for client in clients:
        max_value = 0
        client = client.split()

        # 필요 데이터량이 마지막 plan 데이터 제공량 보다 많은 경우 서비스 불가
        if int(client[0]) > L[-1]:
            result.append(0)
            continue

        # 필요 데이터에 따른 최소 인덱스
        max_value = max(max_value, bisect_left(L, int(client[0])) + 1)

        # 필요 요금제에 따른 최소 인덱스
        for i in client[1:]:
            if dic_additional[i]:
                max_value = max(max_value, dic_additional[i])
            # 필요 요금제가 없는 경우 서비스 불가
            else:
                max_value = 0
                break

        result.append(max_value)

    return result

print(solution(5, ["100 1 3", "500 4", "2000 5"], ["300 3 5", "1500 1", "100 1 3", "50 1 2"]))
print(solution(4, ["38 2 3", "394 1 4"], ["10 2 3", "300 1 2 3 4", "500 1"]))