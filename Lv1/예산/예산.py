def solution(d, budget):
    answer = 0
    count = 0
    d.sort()
    for i in d:
        answer=answer+i
        if answer>budget:
            break
        count+=1
    return count
  
      '''
    1. d를 오름차순으로 sort한다
    2. d의 첫 요소부터 answer에 더한다. 그리고 count를 센다
    3. answer budget을 초과한다면 빠져나온다
    '''
