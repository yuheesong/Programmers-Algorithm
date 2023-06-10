def solution(clothes):
    answer = 1
    h = {}
    for i in clothes:
        if i[1] not in h.keys():
            h[i[1]] = 1
        else:
            h[i[1]] += 1
    for value in h.values():
        answer*=(value+1)
    answer-=1
    return answer
