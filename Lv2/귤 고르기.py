def solution(k, tangerine):
    d={}
    cnt=0
    for i in tangerine:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))        
    for i in d:
        if d[i]>=k:
            cnt+=1
            return cnt
        else:
            k-=d[i]
            cnt+=1
