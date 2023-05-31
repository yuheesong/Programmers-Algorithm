def solution(elements):
    a=[]
    elements2=elements+elements #원형이므로
    n=len(elements) 
    for i in range(n):  
        for j in range(n):  
            s=sum(elements2[j:j+i])
            a.append(s)
    set_a=set(a)
    return len(set_a)
