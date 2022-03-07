def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] *= -1
    return sum(absolutes)


def solution(absolutes, signs):
    return sum([absolutes[i] if signs[i] else absolutes[i]*-1 for i in range(len(absolutes))])