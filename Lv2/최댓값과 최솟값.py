def solution(s):
    answer = ''
    s2=list(map(int, s.split(' ')))
    s2.sort()
    return str(s2[0]) + " " + str(s2[-1])
