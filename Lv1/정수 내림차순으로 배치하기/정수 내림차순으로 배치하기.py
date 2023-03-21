def solution(n):
    n=str(n)
    answer=''.join(sorted(n,reverse=True))
    return int(answer)
