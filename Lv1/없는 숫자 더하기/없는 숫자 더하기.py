def solution(numbers):
    answer = 0
    a=[0,1,2,3,4,5,6,7,8,9]
    for i in numbers:
        if i in a:
            a.remove(i)
    for i in a:
        answer=answer+int(i)
    return answer
