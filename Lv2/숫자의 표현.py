def solution(n):
    answer = 0
    for i in range(1,n+1):
        sum=0
        for j in range(i,n+1):
            sum+=j 
            if sum>n:  #안해줄 시 효율성 검사를 패스하지 못한다
                break
            elif sum==n:
                answer+=1
            else:
                continue
    return answer
