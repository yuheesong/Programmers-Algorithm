def solution(n):
    for i in range(n+1,1000001):
        if str(bin(n)).count('1') == str(bin(i)).count('1'):
            return i
        else:
            continue
