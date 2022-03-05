def solution(sizes):
    max_sizes = []
    min_sizes = []
    
    for size in sizes:
        max_sizes.append(max(size))
        min_sizes.append(min(size))
    
    return max(max_sizes) * max(min_sizes)


#short code
def solution(sizes):
    return max([max(size) for size in sizes]) * max(min(size) for size in sizes)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))