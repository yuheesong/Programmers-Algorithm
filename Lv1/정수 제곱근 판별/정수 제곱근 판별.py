def solution(n):
    result=0
    for i in range(1,n+1):
        if n/i==i:
            return (i+1)*(i+1)
    return -1
