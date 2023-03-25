def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)-4):
        answer=answer+'*'
    for i in phone_number[-4:]:
        answer=answer+i
    return answer
