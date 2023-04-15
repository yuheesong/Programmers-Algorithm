def solution(n, m):
    originN=n
    originM=m
    if n>m:   #n이 작은수, m을 큰수로 함
        n,m = m,n
    while m%n:
        r=m%n
        m=n
        n=r
    return [n, originN*originM/n]
