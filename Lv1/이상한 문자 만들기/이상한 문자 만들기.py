def solution(s):
    answer = ''
    tmp = []
    
    tmp = s.split(" ") # 공백을 기준으로 분리하여 리스트에담기

    for i in range(len(tmp)): 
        for j in range(len(tmp[i])):  
            if tmp[i][j] == " ":
                answer+=" "
            elif j % 2 == 0:
                answer+= tmp[i][j].upper()
            elif j % 2 == 1:
                answer+= tmp[i][j].lower()
        answer+=" "
     
    return answer[0:-1]   #마지막 공백 
