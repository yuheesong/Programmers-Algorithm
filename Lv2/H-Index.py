def solution(citations):
    citations.sort(reverse=True)
    n=len(citations)
    cnt=0
    for i in citations:
        if cnt>=i:
            return cnt
        cnt+=1
    return n