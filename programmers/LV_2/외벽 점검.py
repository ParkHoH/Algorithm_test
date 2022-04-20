def solution(n, weak, dist):
    # dist가 가장 큰 순서부터 weak에서 최대한 많이 포함되는 범위를 구하고
    # weak에서 해당 범위의 원소들을 빼준다.
    # 
    dist.sort()
    cnt = 0
    while dist:
        if not weak:
            break
        distance = dist.pop()
        max_array = []
        for w in weak:
            included_ele = []
            for ele in weak:
                if w+distance <= n:
                    if ele in range(w, w+distance+1):
                        included_ele.append(ele)
                    elif ele >= w+distance+1:
                        break
                else:
                    if ele in range(w, n+1) or ele in range(w+distance+1-n):
                        return
                    
            if len(included_ele) > len(max_array):
                max_array = included_ele
        
        for ele in max_array:
            weak.remove(ele)
        cnt += 1
        
    if weak:
        return -1
    else:
        return cnt

print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))