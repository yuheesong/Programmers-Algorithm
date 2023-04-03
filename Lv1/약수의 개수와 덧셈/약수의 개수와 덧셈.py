def solution(left, right):
    result=0
    for i in range(left,right+1):
        num=0
        for j in range(1,i+1):
            if i%j==0:
                num+=1
        if num%2==0:
            result+=i
        elif num%2==1:
            result-=i
    return result
