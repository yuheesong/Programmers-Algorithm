def solution(n):
    answer = 0
    three=""
    
    while n:
        three+=str(n%3)
        n=n//3
        
    #three 앞뒤반전
    list(three).reverse
    three2=''.join(three)  #three2는 문자열
    
    #10진법으로 변환
    for i in range(len(three)):
        answer+=int(three2[i])*3**(len(three)-1-i)
    return answer
