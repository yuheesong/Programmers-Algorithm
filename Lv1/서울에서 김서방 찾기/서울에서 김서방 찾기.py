def solution(seoul):
    index=0
    count=0
    for i in seoul:
        if i=="Kim":
            index=count
        else:
            count+=1
    return "김서방은 "+str(index)+"에 있다"
