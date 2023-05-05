def solution(brown, yellow):
    total=brown+yellow
    if int((total)**(1/2)) == (total)**(1/2):
        w,h=(total)**(1/2),(total)**(1/2)
    else:
        for i in range(1,brown+5):
            j=(brown+4)/2-i
            if i*j==total:
                w,h=max(i,j),min(i,j)
    return [w,h]
