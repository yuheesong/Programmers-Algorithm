def solution(participant, completion):
    d={}
    sum=0
    for i in participant:
        d[hash(i)]=i
        sum+=hash(i)
    for j in completion:
        sum-=hash(j)
    return d[sum]
