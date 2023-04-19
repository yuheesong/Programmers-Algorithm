def solution(s, n):
    answer=''
    for i in s:
        if i==" ":
            answer+=" "
            continue
        c=ord(i)+n

        if 65<=ord(i)<=90:  #대문자일때
            if c>=91:
                c-=26
        elif 97<=ord(i)<=122:    #소문자일때 
            if c>=123:
                c-=26
        answer+=chr(c)      
    return answer

    '''
        1.공백 처리
        2. 대문자는 대문자끼리
        3. 소문자는 소문자끼리 
        
        대문자에서 소문자로 바뀌는 이슈가 없게 해야함
        '''
