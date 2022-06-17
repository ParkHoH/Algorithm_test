def solution(dist):
    # dist[0] 을 새로운 리스트에 zip 써서 번호 넣어주고 정렬
    L = []
    for i in range(len(dist)):
        L.append([i, dist[0][i]])

    # [1] 부터 len(dist) 까지 거리가 맞는지 검사
    for i in range(1, len(dist)):
        for j in range(i+1, len(dist)):
            max_value = max((L[i][1]), (L[j][1]))
            min_value = min((L[i][1]), (L[j][1]))
            if dist[i][j] != (max_value - min_value):
                L[j][1] *= -1
    L.sort(key=lambda x: x[1])
    result = []
    for i in range(len(L)):
        result.append(L[i][0])

    return [result, result[::-1]] if result[0] < result[::-1][0] else [result[::-1], result]


print(solution([[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]))